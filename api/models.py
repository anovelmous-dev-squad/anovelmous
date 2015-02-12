from django.db import models
from django.contrib.auth.models import User

from .formatting import get_formatted_previous_and_current_novel_tokens, is_allowed_punctuation


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
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Chapter(TimeStampedModel):
    """
    A model consisting of many tokens.
    """
    title = models.CharField(max_length=100)
    novel = models.ForeignKey(Novel, related_name='chapters')
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('title', 'novel')

    def __str__(self):
        return self.title


class Token(TimeStampedModel):
    """
    One of the allowed tokens (word or punctuation) for producing a NovelToken.
    The entire collection is the user vocabulary.
    """
    content = models.CharField(max_length=LONGEST_ENGLISH_WORD_LENGTH, unique=True)
    is_punctuation = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=True)

    def __init__(self, *args, **kwargs):
        super(TimeStampedModel, self).__init__(*args, **kwargs)
        self.is_punctuation = is_allowed_punctuation(self.content)

    def __str__(self):
        return self.content


class AbstractNovelToken(TimeStampedModel):
    ordinal = models.IntegerField()
    chapter = models.ForeignKey(Chapter)

    class Meta:
        abstract = True
        unique_together = ('ordinal', 'chapter')
        ordering = ['ordinal']


class NovelToken(AbstractNovelToken):
    """
    A token tied to a Novel's chapter.
    """
    token = models.ForeignKey(Token)

    def save(self, quote_punctuation_direction=None, *args, **kwargs):
        super(NovelToken, self).save(*args, **kwargs)

        chapter_formatted_tokens = FormattedNovelToken.objects.filter(chapter=self.chapter)
        prev_formatted_novel_token = chapter_formatted_tokens.order_by('-ordinal').first()

        previous_token, new_token = get_formatted_previous_and_current_novel_tokens(
            previous_token=str(prev_formatted_novel_token) if prev_formatted_novel_token else '',
            new_token=str(self),
            quote_punctuation_direction=quote_punctuation_direction
        )

        if previous_token:
            prev_formatted_novel_token.content = previous_token
            prev_formatted_novel_token.save()
        if new_token:
            FormattedNovelToken.objects.create(
                content=new_token,
                ordinal=prev_formatted_novel_token.ordinal+1 if prev_formatted_novel_token else 0,
                chapter=self.chapter
            )

    def __str__(self):
        return self.token.content


class FormattedNovelToken(AbstractNovelToken):
    """
    A token concatenated with surrounding punctuation. This allows for queries to return a space delimited, formatted
    chapter text.
    """
    content = models.CharField(max_length=(LONGEST_ENGLISH_WORD_LENGTH+MAX_PUNCTUATION_LENGTH))

    def __str__(self):
        return self.content


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

    class Meta:
        ordering = ['ordinal']