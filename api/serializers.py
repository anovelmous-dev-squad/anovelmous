__author__ = 'Greg Ziegan'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Novel, Chapter, Token, FormattedNovelToken, Vote


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
        fields = ('id', 'title', 'chapters')


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'novel')


class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ('id', 'content', 'is_punctuation')


class FormattedNovelTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormattedNovelToken
        fields = ('id', 'content', 'ordinal', 'chapter')


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ('id', 'token', 'ordinal', 'selected', 'chapter', 'user')