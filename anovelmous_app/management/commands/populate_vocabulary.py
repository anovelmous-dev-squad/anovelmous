__author__ = 'Greg Ziegan'

from io import BytesIO
import zipfile
import random
import string
from optparse import make_option

from django.core.management.base import BaseCommand
import requests

from api.models import Token
from api.formatting import is_allowed_punctuation


class Command(BaseCommand):
    help = "Populates `Token` table to produce an initial vocabulary for novel writing."
    option_list = BaseCommand.option_list + (
        make_option('--word_cap', type='int',),
    )

    def handle(self, *args, **options):
        word_cap = options.get('word_cap')

        url = 'https://github.com/first20hours/google-10000-english/archive/master.zip'
        common_words_filepath = 'google-10000-english-master/google-10000-english.txt'
        r = requests.get(url)
        stream = BytesIO(r.content)
        zip_file = zipfile.ZipFile(stream)
        with zip_file.open(common_words_filepath) as f:
            vocabulary = [b.decode('utf-8') for b in f.read().splitlines()]

        if word_cap:
            random.shuffle(vocabulary)
            vocabulary = vocabulary[:word_cap]

        for symbol in string.punctuation:
            if is_allowed_punctuation(symbol):
                vocabulary.append(symbol)

        for token in vocabulary:
            Token.objects.create(content=token)