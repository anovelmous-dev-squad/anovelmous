__author__ = 'Greg Ziegan'

from django.apps import AppConfig
from grammar import GrammarFilter
from django.core.cache import cache
from .settings import NLTK_DATA_ABS_PATH

class APIConfig(AppConfig):
    name = 'api'
    verbose_name = 'Anovelmous Application'

    def ready(self):
        token_model = self.get_model('Token')
        try:
            full_vocabulary = list(token_model.objects.all().values_list('content', flat=True))
        except Exception as e:
            # Need to create db first, psycopg's ProgrammingError exception does not bubble up
            return

        gf = GrammarFilter(vocabulary=full_vocabulary, nltk_data_path=NLTK_DATA_ABS_PATH)
        cache.set('grammar_filter', gf)