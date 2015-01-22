__author__ = 'Greg Ziegan'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer
from api.models import Novel, Chapter, Token, NovelToken, FormattedNovelToken


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class NovelSerializer(serializers.HyperlinkedModelSerializer, PaginationSerializer):
    class Meta:
        model = Novel
        fields = ('title', 'next', 'previous', 'count')


class ChapterSerializer(serializers.HyperlinkedModelSerializer, PaginationSerializer):
    class Meta:
        model = Chapter
        fields = ('title', 'next', 'previous', 'count')


class TokenSerializer(serializers.HyperlinkedModelSerializer, PaginationSerializer):
    class Meta:
        model = Token
        fields = ('content', 'is_punctuation', 'next', 'previous', 'count')


class NovelTokenSerializer(serializers.HyperlinkedModelSerializer, PaginationSerializer):
    class Meta:
        model = NovelToken
        fields = ('token', 'ordinal', 'chapter', 'next', 'previous', 'count')


class FormattedNovelTokenSerializer(serializers.HyperlinkedModelSerializer, PaginationSerializer):
    class Meta:
        model = FormattedNovelToken
        fields = ('token', 'ordinal', 'chapter', 'next', 'previous', 'count')