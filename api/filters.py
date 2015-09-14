__author__ = 'Greg Ziegan'
import django_filters

from .models import Contributor, Novel, Chapter, Token, NovelToken, FormattedNovelToken, Vote

class ContributorFilter(django_filters.FilterSet):
    class Meta:
        model = Contributor
        fields = ['username']


class NovelFilter(django_filters.FilterSet):
    class Meta:
        model = Novel
        fields = ['title', 'is_completed']


class ChapterFilter(django_filters.FilterSet):
    novel = django_filters.CharFilter(name='novel__client_id')

    class Meta:
        model = Chapter
        fields = ['title', 'novel', 'is_completed']


class TokenFilter(django_filters.FilterSet):
    class Meta:
        model = Token
        fields = ['is_punctuation', 'is_valid']


class AbstractNovelTokenFilter(django_filters.FilterSet):
    chapter = django_filters.CharFilter(name='chapter__client_id')

    class Meta:
        abstract = True
        fields = ['token', 'chapter']


class NovelTokenFilter(AbstractNovelTokenFilter):
    class Meta:
        model = NovelToken


class FormattedNovelTokenFilter(AbstractNovelTokenFilter):
    class Meta:
        model = FormattedNovelToken


class VoteFilter(django_filters.FilterSet):
    chapter = django_filters.CharFilter(name='chapter__client_id')

    class Meta:
        model = Vote
        fields = ['contributor', 'chapter', 'selected', 'ordinal']
