__author__ = 'Greg Ziegan'
from api.models import NovelToken, Novel
from time import sleep
from django.db import connection
from django.core.management.base import NoArgsCommand
VOTING_PERIOD = 15


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        most_recent_chapter = Novel.objects.order_by('-id').first().chapters.last()
        current_novel_token = NovelToken.objects.filter(chapter=most_recent_chapter).order_by('-ordinal').first()
        ordinal = current_novel_token.ordinal + 1

        while True:
            sleep(VOTING_PERIOD)
            self.insert_most_popular_token(most_recent_chapter.id, ordinal)

    @staticmethod
    def insert_most_popular_token(self, chapter_id, ordinal):
        """
        Will select the most popular, grammatically correct vote during the last 10 seconds.
        """
        cursor = connection.cursor()
        query = '''SELECT V.token_id
                   FROM api_vote V
                   WHERE V.chapter_id = %s AND V.ordinal = %s
                   GROUP BY V.token_id
                   ORDER BY token_count DESC
                   LIMIT 1'''

        cursor.execute(query, [chapter_id, ordinal])
        most_popular_token_id = cursor.fetchone()

        if not most_popular_token_id:
            return

        NovelToken(
            token=most_popular_token_id,
            ordinal=ordinal,
            chapter_id=chapter_id
        ).objects.create()
