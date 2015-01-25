__author__ = 'Greg Ziegan'

from django.apps import AppConfig
from grammar import GrammarFilter
from api.models import Token
from django.core.cache import cache
from .settings import NLTK_DATA_ABS_PATH


class APIConfig(AppConfig):
    name = 'anovelmous_app'
    verbose_name = 'Anovelmous Application'

    def ready(self):
        full_vocabulary = list(Token.objects.all().values_list('content', flat=True))
        gf = GrammarFilter(vocabulary=full_vocabulary, nltk_data_path=NLTK_DATA_ABS_PATH)
        cache.set('grammar_filter', gf)