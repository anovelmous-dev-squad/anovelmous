__author__ = 'Greg Ziegan'

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Novel, Chapter, Token, NovelToken, FormattedNovelToken, Vote, Contributor, Guild


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class ContributorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contributor
        fields = ('client_id', 'url', 'username', 'email', 'date_joined')
        extra_kwargs = {
            'url': {'view_name': 'contributor-detail', 'lookup_field': 'client_id'},
        }


class ContributorModifySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contributor
        fields = ('client_id', 'url', 'username', 'email')
        extra_kwargs = {
            'url': {'view_name': 'contributor-detail', 'lookup_field': 'client_id'},
        }


class GuildSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guild
        fields = ('client_id', 'url', 'name')
        extra_kwargs = {
            'url': {'view_name': 'guild-detail', 'lookup_field': 'client_id'},
        }


class NovelSerializer(serializers.HyperlinkedModelSerializer):
    chapters = serializers.HyperlinkedIdentityField(
        view_name='chapter-list',
        lookup_field='client_id',
        lookup_url_kwarg='novel_client_id'
    )

    class Meta:
        model = Novel
        fields = ('client_id', 'url', 'title', 'is_completed', 'chapters', 'voting_duration', 'created_at')
        extra_kwargs = {
            'url': {'view_name': 'novel-detail', 'lookup_field': 'client_id'},
        }


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    novel_tokens = serializers.HyperlinkedIdentityField(
        view_name='noveltoken-list',
        lookup_url_kwarg='chapter_client_id',
        lookup_field='client_id'
    )

    formatted_novel_tokens = serializers.HyperlinkedIdentityField(
        view_name='formattednoveltoken-list',
        lookup_url_kwarg='chapter_client_id',
        lookup_field='client_id'
    )

    class Meta:
        model = Chapter
        fields = ('client_id', 'url', 'title', 'is_completed', 'novel', 'novel_tokens', 'formatted_novel_tokens', 'created_at')
        extra_kwargs = {
            'url': {'view_name': 'chapter-detail', 'lookup_field': 'client_id'},
            'novel': {'view_name': 'novel-detail', 'lookup_field': 'client_id'}
        }


class TokenSerializer(DynamicFieldsModelSerializer, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Token
        fields = ('client_id', 'url', 'content', 'is_valid', 'is_punctuation', 'created_at')
        extra_kwargs = {
            'url': {'view_name': 'token-detail', 'lookup_field': 'client_id'},
        }


class NovelTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NovelToken
        fields = ('client_id', 'url', 'ordinal', 'chapter', 'token', 'created_at')
        extra_kwargs = {
            'url': {'view_name': 'noveltoken-detail', 'lookup_field': 'client_id'},
            'chapter': {'view_name': 'chapter-detail', 'lookup_field': 'client_id'},
            'token': {'view_name': 'token-detail', 'lookup_field': 'client_id'}
        }


class FormattedNovelTokenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormattedNovelToken
        fields = ('client_id', 'url', 'content', 'ordinal', 'chapter', 'created_at')
        extra_kwargs = {
            'url': {'view_name': 'formattednoveltoken-detail', 'lookup_field': 'client_id'},
            'chapter': {'view_name': 'chapter-detail', 'lookup_field': 'client_id'}
        }


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ('client_id', 'url', 'ordinal', 'selected', 'chapter', 'token', 'contributor', 'created_at')
        extra_kwargs = {
            'url': {'view_name': 'vote-detail', 'lookup_field': 'client_id'},
            'chapter': {'view_name': 'chapter-detail', 'lookup_field': 'client_id'},
            'token': {'view_name': 'token-detail', 'lookup_field': 'client_id'},
            'contributor': {'view_name': 'contributor-detail', 'lookup_field': 'client_id'},
        }


class VoteModifySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ('client_id', 'url', 'chapter', 'token', 'ordinal')
        read_only_fields = ('contributor',)
        extra_kwargs = {
            'url': {'view_name': 'vote-detail', 'lookup_field': 'client_id'},
            'chapter': {'view_name': 'chapter-detail', 'lookup_field': 'client_id'},
            'token': {'view_name': 'token-detail', 'lookup_field': 'client_id'}
        }

