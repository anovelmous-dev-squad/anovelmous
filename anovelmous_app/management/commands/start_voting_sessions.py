__author__ = 'Greg Ziegan'
from api.models import NovelToken, Novel, Vote
from time import sleep
from django.db import connection
from django.core.management.base import NoArgsCommand

import logging
logger = logging.getLogger(__name__)


VOTING_PERIOD = 15


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        while True:
            most_recent_chapter = Novel.objects.order_by('-id').first().chapters.last()
            current_novel_token = NovelToken.objects.filter(chapter=most_recent_chapter).last()
            if not current_novel_token:
                ordinal = 1
            else:
                ordinal = current_novel_token.ordinal + 1
            self.insert_most_popular_token(most_recent_chapter.id, ordinal)
            sleep(VOTING_PERIOD)

    @staticmethod
    def insert_most_popular_token(chapter_id, ordinal):
        """
        Will select the most popular, grammatically correct vote during the last 10 seconds.
        """
        cursor = connection.cursor()
        query = '''SELECT V.token_id, COUNT(V) as token_count
                   FROM api_vote V
                   WHERE V.chapter_id = %s AND V.ordinal = %s
                   GROUP BY V.token_id
                   ORDER BY token_count DESC
                   LIMIT 1'''

        cursor.execute(query, [chapter_id, ordinal])
        most_popular_token = cursor.fetchone()

        if not most_popular_token:
            return

        most_popular_token_id = most_popular_token[0]

        new_novel_token = NovelToken.objects.create(
            token_id=most_popular_token_id,
            ordinal=ordinal,
            chapter_id=chapter_id
        )

        Vote.objects.filter(chapter_id=chapter_id, ordinal=ordinal, token_id=most_popular_token_id)\
            .update(selected=True)

        logger.debug("Created new `NovelToken`: {}".format(new_novel_token))