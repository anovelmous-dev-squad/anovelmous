from django.contrib.auth.models import User, Group
from django.http import HttpResponse

from .models import Novel, Chapter, Token, NovelToken, FormattedNovelToken, Vote

from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.pagination import PageNumberPagination
from .serializers import UserSerializer, UserModifySerializer, GroupSerializer, NovelSerializer, \
    ChapterListSerializer, ChapterDetailSerializer, TokenSerializer, NovelTokenSerializer, \
    FormattedNovelTokenSerializer, VoteSerializer, VoteModifySerializer

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework_extensions.mixins import PaginateByMaxMixin

from django.core.cache import cache

import logging
logging.basicConfig(filename='api.log', level=logging.DEBUG)


class AuthMixin(object):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class UserViewSet(viewsets.ReadOnlyModelViewSet,
                  mixins.UpdateModelMixin,
                  AuthMixin,
                  PaginateByMaxMixin):
    """
    This endpoint presents the `User` resource.

    Given an account, a user may edit the details of only their own instance.
    However, any user may view the public information about any other user.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    max_paginate_by = 50
    filter_fields = ('username',)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserSerializer
        else:
            return UserModifySerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
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
    filter_fields = ('title', 'is_completed')


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
    serializer_class = ChapterListSerializer
    lookup_field = 'client_id'
    max_paginate_by = 100
    filter_fields = ('title', 'novel', 'is_completed')

    def get_queryset(self):
        novel_pk = self.kwargs.get('novel_pk')
        if novel_pk:
            queryset = Chapter.objects.filter(novel__id=novel_pk)
        else:
            queryset = Chapter.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ChapterDetailSerializer
        else:
            return ChapterListSerializer


class TokenViewSet(viewsets.ReadOnlyModelViewSet,
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
    filter_fields = ('is_punctuation', 'is_valid')

    @list_route(methods=['GET'])
    def filter_on_grammar(self, request):
        gf = cache.get('grammar_filter')
        most_recent_novel_token = NovelToken.objects.last()
        tokens = gf.get_grammatically_correct_vocabulary_subset(str(most_recent_novel_token))
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(tokens, request)
        return paginator.get_paginated_response(result_page)


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
    filter_fields = ('token', 'chapter')

    def get_queryset(self):
        chapter_pk = self.kwargs.get('chapter_pk')
        if chapter_pk:
            queryset = NovelToken.objects.filter(chapter__id=chapter_pk)
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
    filter_fields = ('content', 'chapter')

    def get_queryset(self):
        chapter_pk = self.kwargs.get('chapter_pk')
        if chapter_pk:
            queryset = FormattedNovelToken.objects.filter(chapter__id=chapter_pk)
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
    filter_fields = ('user', 'chapter', 'selected', 'ordinal')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VoteSerializer
        else:
            return VoteModifySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def index(request):
    return HttpResponse('Anovelmous')