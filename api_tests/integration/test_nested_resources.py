__author__ = 'Greg Ziegan'

import pytest
from api.models import Novel, Chapter, Token, NovelToken

pytestmark = pytest.mark.django_db

@pytest.fixture
def client():
    from rest_framework.test import APIClient
    return APIClient()

def test_novel_nested_resources(client):
    novel1 = Novel.objects.create(title='Test Novel Alpha')
    novel2 = Novel.objects.create(title='Test Novel Beta')
    Chapter.objects.create(title='Chapter One', novel=novel1, is_completed=True)
    Chapter.objects.create(title='Chapter Two', novel=novel1)
    num_novel_one_chapters = 2
    Chapter.objects.create(title='Chapter 1', novel=novel2)

    novel_response = client.get('/api/novels/{}/'.format(novel1.client_id))
    novel_chapters_url = novel_response.data['chapters']
    chapters_response = client.get(novel_chapters_url)
    chapters_response_query = client.get('/api/chapters/?novel={}'.format(novel1.client_id))

    assert len(chapters_response.data) == len(chapters_response_query.data)
    assert len(chapters_response.data) == num_novel_one_chapters

def test_chapter_nested_resources(client):
    novel = Novel.objects.create(title='Test Novel Charlie')
    chapter1 = Chapter.objects.create(title='Chapter One', novel=novel, is_completed=True)
    chapter2 = Chapter.objects.create(title='Chapter Two', novel=novel)
    token1 = Token.objects.create(content="i")
    token2 = Token.objects.create(content="am")
    token3 = Token.objects.create(content="test")
    NovelToken.objects.create(token=token1, chapter=chapter1, ordinal=0)
    NovelToken.objects.create(token=token2, chapter=chapter1, ordinal=1)
    num_chapter1_novel_tokens = 2
    num_chapter1_formatted_novel_tokens = 2
    NovelToken.objects.create(token=token3, chapter=chapter2, ordinal=0)

    chapter_response = client.get('/api/chapters/{}/'.format(chapter1.client_id))
    chapter_novel_tokens_url = chapter_response.data['novel_tokens']
    novel_tokens_response = client.get(chapter_novel_tokens_url)

    novel_token_response_query = client.get('/api/novel_tokens/?chapter={}'.format(chapter1.client_id))

    assert len(novel_tokens_response.data) == len(novel_token_response_query.data)
    assert len(novel_tokens_response.data) == num_chapter1_novel_tokens

    chapter_formatted_novel_tokens_url = chapter_response.data['formatted_novel_tokens']
    formatted_novel_tokens_response = client.get(chapter_formatted_novel_tokens_url)
    formatted_novel_tokens_res_query = client.get('/api/formatted_novel_tokens/?chapter={}'.format(chapter1.client_id))

    assert len(formatted_novel_tokens_response.data) == len(formatted_novel_tokens_res_query.data)
    assert len(formatted_novel_tokens_response.data) == num_chapter1_formatted_novel_tokens

