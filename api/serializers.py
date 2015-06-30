__author__ = 'Greg Ziegan'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Novel, Chapter, Token, NovelToken, FormattedNovelToken, Vote


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('client_id', 'url', 'username', 'email', 'groups', 'date_joined')

class UserModifySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('client_id', 'url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('client_id', 'url', 'name')


class NovelSerializer(serializers.HyperlinkedModelSerializer):
    chapters = serializers.HyperlinkedIdentityField(view_name='chapter-list', lookup_url_kwarg='novel_pk')

    class Meta:
        model = Novel
        fields = ('client_id', 'url', 'title', 'is_completed', 'chapters', 'voting_duration', 'created_at')


class ChapterListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ('client_id', 'url', 'title', 'is_completed', 'novel', 'voting_duration', 'created_at')


class ChapterDetailSerializer(serializers.HyperlinkedModelSerializer):
    novel_tokens = serializers.HyperlinkedIdentityField(view_name='noveltoken-list', lookup_url_kwarg='chapter_pk')
    formatted_novel_tokens = serializers.HyperlinkedIdentityField(
        view_name='formattednoveltoken-list',
        lookup_url_kwarg='chapter_pk'
    )

    class Meta:
        model = Chapter
        fields = ('client_id', 'url', 'title', 'is_completed', 'novel', 'novel_tokens', 'formatted_novel_tokens', 'created_at')


class TokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ('client_id', 'url', 'content', 'is_valid', 'is_punctuation', 'created_at')


class NovelTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NovelToken
        fields = ('client_id', 'url', 'token', 'ordinal', 'chapter', 'created_at')


class FormattedNovelTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormattedNovelToken
        fields = ('client_id', 'url', 'content', 'ordinal', 'chapter', 'created_at')


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ('client_id', 'url', 'token', 'ordinal', 'selected', 'chapter', 'user', 'created_at')


class VoteModifySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ('client_id', 'url', 'token', 'ordinal', 'chapter')
        read_only_fields = ('user',)

