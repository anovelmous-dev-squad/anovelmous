__author__ = 'Greg Ziegan'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Novel, Chapter, Token, FormattedNovelToken, Vote


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class NovelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Novel
        fields = ('id', 'title', 'is_completed', 'url')


class NovelChapterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Novel
        fields = ('id', 'title', 'is_completed', 'chapters', 'url')
        depth = 1


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    novel_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Chapter
        fields = ('id', 'title', 'is_completed', 'novel', 'novel_id', 'url')


class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ('id', 'url', 'content', 'is_valid', 'is_punctuation')


class FormattedNovelTokenSerializer(serializers.HyperlinkedModelSerializer):
    chapter_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = FormattedNovelToken
        fields = ('id', 'url', 'content', 'ordinal', 'chapter', 'chapter_id')


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    chapter_id = serializers.PrimaryKeyRelatedField(read_only=True)
    token_id = serializers.PrimaryKeyRelatedField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Vote
        fields = ('id', 'url', 'token', 'token_id', 'ordinal', 'selected', 'chapter', 'chapter_id', 'user', 'user_id')