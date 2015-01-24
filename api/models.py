from django.db import models
from django.contrib.auth.models import User, Group
import string

LONGEST_ENGLISH_WORD_LENGTH = 28
MAX_PUNCTUATION_LENGTH = 7


class TimeStampedModel(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Novel(TimeStampedModel):
    """
    A model consisting of chapters of dynamic content.
    """
    title = models.CharField(max_length=100, unique=True)


class Chapter(TimeStampedModel):
    """
    A model consisting of many tokens.
    """
    title = models.CharField(max_length=100)
    novel = models.ForeignKey(Novel)

    class Meta:
        unique_together = ('title', 'novel')


class Token(TimeStampedModel):
    """
    One of the allowed tokens (word or punctuation) for producing a NovelToken.
    The entire collection is the user vocabulary.
    """
    content = models.CharField(max_length=LONGEST_ENGLISH_WORD_LENGTH, unique=True)
    is_punctuation = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(TimeStampedModel, self).__init__(*args, **kwargs)
        self.is_punctuation = self.is_allowed_punctuation(self.content)

    @classmethod
    def is_allowed_punctuation(cls, symbol):
        return symbol in '!"$%&\'(),.:;?'


class AbstractNovelToken(TimeStampedModel):
    ordinal = models.IntegerField()
    chapter = models.ForeignKey(Chapter)

    class Meta:
        abstract = True


class NovelToken(AbstractNovelToken):
    """
    A token tied to a Novel's chapter.
    """
    token = models.ForeignKey(Token)


class FormattedNovelToken(AbstractNovelToken):
    """
    A token concatenated with surrounding punctuation. This allows for queries to return a space delimited, formatted
    chapter text.
    """
    token = models.CharField(max_length=(LONGEST_ENGLISH_WORD_LENGTH+MAX_PUNCTUATION_LENGTH))



class Vote(TimeStampedModel):
    """
    A model used to cast a vote for a new NovelToken. The most popular vote during the voting window will determine the
    next NovelToken.
    """
    token = models.ForeignKey(Token)
    ordinal = models.IntegerField()
    selected = models.BooleanField(default=False)
    chapter = models.ForeignKey(Chapter)
    user = models.ForeignKey(User)