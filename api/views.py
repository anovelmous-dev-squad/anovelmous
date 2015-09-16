from django.core.cache import cache
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework_extensions.mixins import PaginateByMaxMixin

from .models import Novel, Chapter, Token, NovelToken, FormattedNovelToken, Vote, Contributor, Guild
from .serializers import ContributorSerializer, ContributorModifySerializer, GuildSerializer, NovelSerializer, \
    ChapterSerializer, TokenSerializer, NovelTokenSerializer, \
    FormattedNovelTokenSerializer, VoteSerializer, VoteModifySerializer
from .filters import ContributorFilter, NovelFilter, ChapterFilter, TokenFilter, NovelTokenFilter, \
    FormattedNovelTokenFilter, VoteFilter

import logging

log = logging.getLogger('logentries')
log.setLevel(logging.INFO)

class AuthMixin(object):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

class DynamicFieldsViewMixin(object):
    def get_serializer(self, *args, **kwargs):

        serializer_class = self.get_serializer_class()

        fields = None
        if self.request.method == 'GET':
            query_fields = self.request.query_params.get("fields", None)

            if query_fields:
                fields = tuple(query_fields.split(','))

        kwargs['context'] = self.get_serializer_context()
        kwargs['fields'] = fields

        return serializer_class(*args, **kwargs)


class ContributorViewSet(viewsets.ReadOnlyModelViewSet,
                         mixins.UpdateModelMixin,
                         AuthMixin,
                         PaginateByMaxMixin):
    """
    This endpoint presents the `User` resource.

    Given an account, a user may edit the details of only their own instance.
    However, any user may view the public information about any other user.

    """
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    lookup_field = 'client_id'
    max_paginate_by = 50
    filter_class = ContributorFilter

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return ContributorSerializer
        else:
            return ContributorModifySerializer


class GuildViewSet(viewsets.ReadOnlyModelViewSet,
                   mixins.UpdateModelMixin,
                   AuthMixin, PaginateByMaxMixin):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    lookup_field = 'client_id'
    max_paginate_by = 10


class NovelViewSet(viewsets.ReadOnlyModelViewSet, AuthMixin, PaginateByMaxMixin):
    """
    This endpoint presents the `Novel` resource.

    A `Novel` is a collection of `Chapter`s encompassing a complete narrative.
    Through collaborative writing, many of these will be produced, however the ability to create
    a new novel is delegated to the backend implementation.

    If a single user is able to create a new `Novel` at any time, chaos would ensue.

    """
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
    lookup_field = 'client_id'
    max_paginate_by = 100
    filter_class = NovelFilter


class ChapterViewSet(viewsets.ReadOnlyModelViewSet, AuthMixin, PaginateByMaxMixin):
    """
    This endpoint presents the `Chapter` resource.

    A `Chapter` is a segment of the `Novel` narrative, filled with words and punctuation.
    In order to model these words, punctuations, and their formatting, two other resources
    are tied to the `Chapter` resource.

    The `NovelToken` and the `FormattedNovelToken` make up the `Chapter`'s content.
    The former is the series of tokens making up the story while the latter is the series
    of space-delimited word/punctuation combinations making up the `Chapter`.

    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    lookup_field = 'client_id'
    max_paginate_by = 100
    filter_class = ChapterFilter

    def get_queryset(self):
        novel_client_id = self.kwargs.get('novel_client_id')
        if novel_client_id:
            queryset = Chapter.objects.filter(novel__client_id=novel_client_id)
        else:
            queryset = Chapter.objects.all()
        return queryset


class TokenViewSet(DynamicFieldsViewMixin,
                   viewsets.ReadOnlyModelViewSet,
                   mixins.UpdateModelMixin,
                   AuthMixin,
                   PaginateByMaxMixin):
    """
    This endpoint presents the `Token` resource.

    A `Token` is an allowed vocabulary term. It can be a punctuation or a word.
    The `Token` vocabulary is able to expand based upon the rules set forth by
    the backend designers.

    The current motivation of making the vocabulary set dynamic is to reward
    devoted contributors with the ability to add new vocabulary terms.

    """
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    lookup_field = 'client_id'
    max_paginate_by = 100
    filter_class = TokenFilter

    def get_queryset(self):
        queryset = Token.objects.all()
        filter_on_grammar = self.request.query_params.get('filter_on_grammar', False)
        if filter_on_grammar:
            gf = cache.get('grammar_filter')
            most_recent_novel_token = NovelToken.objects.last()
            tokens = gf.get_grammatically_correct_vocabulary_subset(str(most_recent_novel_token))
            queryset = queryset.filter(content__in=tokens)
        return queryset


class NovelTokenViewSet(viewsets.ReadOnlyModelViewSet, AuthMixin, PaginateByMaxMixin):
    """
    This endpoint presents the `NovelToken` resource.

    A `NovelToken` is essentially the most popular `Token` among users at a given position
    in the `Chapter`. It is created by the backend system at the end of a voting round and
    then also used to create the next `FormattedNovelToken`.

    """
    queryset = NovelToken.objects.all()
    serializer_class = NovelTokenSerializer
    lookup_field = 'client_id'
    max_paginate_by = 100
    filter_class = NovelTokenFilter

    def get_queryset(self):
        chapter_client_id = self.kwargs.get('chapter_client_id')
        if chapter_client_id:
            queryset = NovelToken.objects.filter(chapter__client_id=chapter_client_id)
        else:
            queryset = NovelToken.objects.all()
        return queryset


class FormattedNovelTokenViewSet(viewsets.ReadOnlyModelViewSet, AuthMixin, PaginateByMaxMixin):
    """
    This endpoint presents the `FormattedNovelToken` resource.

    A `FormattedNovelToken` is a `NovelToken` with appended or prepended punctuation based on the
    textual context.

    """
    queryset = FormattedNovelToken.objects.all()
    serializer_class = FormattedNovelTokenSerializer
    lookup_field = 'client_id'
    max_paginate_by = 100
    filter_class = FormattedNovelTokenFilter

    def get_queryset(self):
        chapter_client_id = self.kwargs.get('chapter_client_id')
        if chapter_client_id:
            queryset = FormattedNovelToken.objects.filter(chapter__client_id=chapter_client_id)
        else:
            queryset = FormattedNovelToken.objects.all()
        return queryset


class VoteViewSet(viewsets.ReadOnlyModelViewSet,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  AuthMixin,
                  PaginateByMaxMixin):
    """
    This endpoint presents the `Vote` resource.

    A `Vote` is a selection of a vocabulary term (a `Token`) by a single Anovelmous `User` as a candidate
    `NovelToken` in the story thus far.

    The backend will decide what `Vote`s become part of the story and also the length of the voting rounds.

    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    lookup_field = 'client_id'
    max_paginate_by = 100
    filter_class = VoteFilter

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return VoteSerializer
        else:
            return VoteModifySerializer

    def perform_create(self, serializer):
        serializer.save(contributor=Contributor.objects.get(user_ptr=self.request.user))


def index(request):
    return HttpResponse('Anovelmous')
