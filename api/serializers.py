__author__ = 'Greg Ziegan'

from django.contrib.auth.models import User, Group
from rest_framework import serializers, pagination
from api.models import Novel, Chapter, Token, NovelToken, FormattedNovelToken


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = ('id', 'title',)


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title',)


class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ('id', 'content', 'is_punctuation')


class NovelTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NovelToken
        fields = ('id', 'token', 'ordinal', 'chapter')


class FormattedNovelTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormattedNovelToken
        fields = ('id', 'token', 'ordinal', 'chapter')