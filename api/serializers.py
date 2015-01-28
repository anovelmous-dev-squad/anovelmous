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


class NovelChapterListingField(serializers.RelatedField):
    def to_representation(self, value):
        serializer = ChapterPkAndURLSerializer(value, context=self.context)
        return serializer.data


class NovelSerializer(serializers.ModelSerializer):
    """chapters = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='chapter-detail'
    )"""
    chapters = NovelChapterListingField(read_only=True, many=True)

    class Meta:
        model = Novel
        fields = ('id', 'title', 'chapters')


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'novel')


class ChapterPkAndURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'url')


class TokenSerializer(serializers.HyperlinkedModelSerializer):
    lookup_field = 'content'

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