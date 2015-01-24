from django.contrib.auth.models import User, Group
from django.http import HttpResponse

from api.models import Novel, Chapter, Token, NovelToken, FormattedNovelToken

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.pagination import PaginationSerializer
from api.serializers import UserSerializer, GroupSerializer, NovelSerializer, \
    ChapterSerializer, TokenSerializer, NovelTokenSerializer, FormattedNovelTokenSerializer

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_extensions.mixins import PaginateByMaxMixin

from django.core.cache import cache
from django.core.paginator import Paginator

import logging
logger = logging.getLogger('view_logger')


class AuthMixin(object):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class UserViewSet(viewsets.ModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    max_paginate_by = 50


class GroupViewSet(viewsets.ModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    max_paginate_by = 10


class NovelViewSet(viewsets.ModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer
    max_paginate_by = 100


class ChapterViewSet(viewsets.ModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer
    max_paginate_by = 100


class TokenViewSet(viewsets.ModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer
    max_paginate_by = 100

    @list_route(methods=['GET'])
    def filter_on_grammar(self, request):
        gf = cache.get('grammar_filter')
        most_recent_novel_token = NovelToken.objects.last()
        tokens = gf.get_grammatically_correct_vocabulary_subset(str(most_recent_novel_token))
        paginator = Paginator(tokens, 100)
        page = paginator.page(request.query_params.get('page', 1))
        serializer = PaginationSerializer(instance=page, context={'request': request})
        return Response(serializer.data)


class NovelTokenViewSet(viewsets.ModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = NovelToken.objects.all()
    serializer_class = NovelTokenSerializer
    max_paginate_by = 100


class FormattedNovelTokenViewSet(viewsets.ModelViewSet, AuthMixin, PaginateByMaxMixin):
    queryset = FormattedNovelToken.objects.all()
    serializer_class = FormattedNovelTokenSerializer
    max_paginate_by = 100


def index(request):
    logger.debug(request.META['HTTP_HOST'])
    return HttpResponse('Anovelmous')