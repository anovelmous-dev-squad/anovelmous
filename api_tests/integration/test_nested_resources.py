__author__ = 'Greg Ziegan'

from api.views import NovelViewSet, ChapterViewSet, NovelTokenViewSet, FormattedNovelTokenViewSet

import pytest

@pytest.fixture
def client():
    from rest_framework.test import APIClient
    return APIClient()

def test_novel_chapters_relationship(client):
    novels_response = client.get('/api/novels/')
    first_novel = novels_response.data[0]
    novel_chapters_url = first_novel.chapters
    chapters_response = client.get(novel_chapters_url)
