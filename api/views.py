from django.contrib.auth.models import User, Group
from api.models import Novel, Chapter, Token, NovelToken, FormattedNovelToken
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, NovelSerializer, \
    ChapterSerializer, TokenSerializer, NovelTokenSerializer, FormattedNovelTokenSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class NovelViewSet(viewsets.ModelViewSet):
    queryset = Novel.objects.all()
    serializer_class = NovelSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class TokenViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer


class NovelTokenViewSet(viewsets.ModelViewSet):
    queryset = NovelToken.objects.all()
    serializer_class = NovelTokenSerializer


class FormattedNovelTokenViewSet(viewsets.ModelViewSet):
    queryset = FormattedNovelToken.objects.all()
    serializer_class = FormattedNovelTokenSerializer