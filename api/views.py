from django.contrib.auth.models import User, Group
from django.http import HttpResponse

from .models import Novel, Chapter, Token, NovelToken, FormattedNovelToken, Vote

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.pagination import PaginationSerializer
from .serializers import UserSerializer, GroupSerializer, NovelSerializer, NovelChapterSerializer, \
    ChapterSerializer, TokenSerializer, NovelTokenSerializer, \
    FormattedNovelTokenSerializer, VoteSerializer, VoteModifySerializer

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework_extensions.mixins import PaginateByMaxMixin

from django.core.cache import cache
from django.core.paginator import Paginator

import logging
logging.basicConfig(filename='api.log', level=logging.DEBUG)


class AuthMixin(object):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class UserViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  AuthMixin,
                  PaginateByMaxMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    max_paginate_by = 50
    filter_fields = ('username',)


class GroupViewSet(viewsets.ReadOnlyModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    max_paginate_by = 10


class NovelViewSet(viewsets.ReadOnlyModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
    max_paginate_by = 100
    filter_fields = ('title', 'is_completed')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return NovelChapterSerializer
        else:
            return NovelSerializer


class ChapterViewSet(viewsets.ReadOnlyModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    max_paginate_by = 100
    filter_fields = ('title', 'novel', 'is_completed')


class TokenViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin,
                   AuthMixin,
                   PaginateByMaxMixin):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    max_paginate_by = 100
    filter_fields = ('is_punctuation', 'is_valid')

    @list_route(methods=['GET'])
    def filter_on_grammar(self, request):
        gf = cache.get('grammar_filter')
        most_recent_novel_token = NovelToken.objects.last()
        tokens = gf.get_grammatically_correct_vocabulary_subset(str(most_recent_novel_token))
        paginator = Paginator(tokens, 100)
        page = paginator.page(request.query_params.get('page', 1))
        serializer = PaginationSerializer(instance=page, context={'request': request})
        return Response(serializer.data)


class NovelTokenViewSet(viewsets.ReadOnlyModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = NovelToken.objects.all()
    serializer_class = NovelTokenSerializer
    max_paginate_by = 100
    filter_fields = ('token', 'chapter')


class FormattedNovelTokenViewSet(viewsets.ReadOnlyModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = FormattedNovelToken.objects.all()
    serializer_class = FormattedNovelTokenSerializer
    max_paginate_by = 100
    filter_fields = ('content', 'chapter')


class VoteViewSet(viewsets.ModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    max_paginate_by = 100
    filter_fields = ('user', 'chapter', 'selected', 'ordinal')

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return VoteSerializer
        else:
            return VoteModifySerializer


def index(request):
    return HttpResponse('Anovelmous')