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
            most_recent_chapter = Novel.objects.filter(stage__name='WRITING').order_by('-id').first().chapters.last()
            current_novel_token = NovelToken.objects.filter(chapter=most_recent_chapter).last()
            if not current_novel_token:
                ordinal = 0
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
        query = '''SELECT V.token_id, V.character_id, V.plot_item_id, V.place_id, COUNT(V) as token_count
                   FROM api_vote V
                   WHERE V.chapter_id = %s AND V.ordinal = %s
                   GROUP BY V.token_id, V.character_id, V.plot_item_id, V.place_id
                   ORDER BY token_count DESC
                   LIMIT 1'''

        cursor.execute(query, [chapter_id, ordinal])
        most_popular_token = cursor.fetchone()

        if not most_popular_token:
            return

        relation_args = {}
        if most_popular_token[0]:
            relation_args['token_id'] = most_popular_token[0]
        elif most_popular_token[1]:
            relation_args['character_id'] = most_popular_token[1]
        elif most_popular_token[2]:
            relation_args['plot_item_id'] = most_popular_token[2]
        elif most_popular_token[3]:
            relation_args['place_id'] = most_popular_token[3]

        new_novel_token = NovelToken.objects.create(
            ordinal=ordinal,
            chapter_id=chapter_id,
            **relation_args
        )

        Vote.objects.filter(chapter_id=chapter_id, ordinal=ordinal, **relation_args)\
            .update(selected=True)

        logger.debug("Created new `NovelToken`: {}".format(new_novel_token))
