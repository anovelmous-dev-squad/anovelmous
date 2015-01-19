from django.contrib.auth.models import User, Group
from django.http import HttpResponse

from api.models import Novel, Chapter, Token, NovelToken, FormattedNovelToken

from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, NovelSerializer, \
    ChapterSerializer, TokenSerializer, NovelTokenSerializer, FormattedNovelTokenSerializer

from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import logging
logging.basicConfig(filename='api.log', level=logging.DEBUG)


class AuthMixin(object):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)


class UserViewSet(viewsets.ModelViewSet, AuthMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet, AuthMixin):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class NovelViewSet(viewsets.ModelViewSet, AuthMixin):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer


class ChapterViewSet(viewsets.ModelViewSet, AuthMixin):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class TokenViewSet(viewsets.ModelViewSet, AuthMixin):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class NovelTokenViewSet(viewsets.ModelViewSet, AuthMixin):
    queryset = NovelToken.objects.all()
    serializer_class = NovelTokenSerializer


class FormattedNovelTokenViewSet(viewsets.ModelViewSet, AuthMixin):
    queryset = FormattedNovelToken.objects.all()
    serializer_class = FormattedNovelTokenSerializer


def index(request):
    print('HTTP HOST: {}'.format(request.META['HTTP_HOST']))
    return HttpResponse('Anovelmous')