__author__ = 'Greg Ziegan'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Novel, Chapter, Token, NovelToken, FormattedNovelToken, Vote


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class NovelSerializer(serializers.HyperlinkedModelSerializer):
    chapters = serializers.HyperlinkedIdentityField(view_name='chapter-list', lookup_url_kwarg='novel_pk')

    class Meta:
        model = Novel
        fields = ('url', 'title', 'is_completed', 'chapters')


class ChapterListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ('url', 'title', 'is_completed', 'novel')


class ChapterDetailSerializer(serializers.HyperlinkedModelSerializer):
    novel_tokens = serializers.HyperlinkedIdentityField(view_name='noveltoken-list', lookup_url_kwarg='chapter_pk')
    formatted_novel_tokens = serializers.HyperlinkedIdentityField(
        view_name='formattednoveltoken-list',
        lookup_url_kwarg='chapter_pk'
    )

    class Meta:
        model = Chapter
        fields = ('url', 'title', 'is_completed', 'novel', 'novel_tokens', 'formatted_novel_tokens')


class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ('url', 'content', 'is_valid', 'is_punctuation')


class NovelTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NovelToken
        fields = ('url', 'token', 'ordinal', 'chapter', 'created_at')


class FormattedNovelTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormattedNovelToken
        fields = ('url', 'content', 'ordinal', 'chapter')


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ('url', 'token', 'ordinal', 'selected', 'chapter', 'user')


class VoteModifySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ('url', 'token', 'ordinal', 'chapter', 'user')

