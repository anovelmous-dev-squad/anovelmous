__author__ = 'Greg Ziegan'

import pytest
from api.models import Novel, Chapter

pytestmark = pytest.mark.django_db

@pytest.fixture
def client():
    from rest_framework.test import APIClient
    return APIClient()

def test_novel_chapters_relationship(client):
    novel = Novel.objects.create(title='Test Novel Alpha')
    novel_two = Novel.objects.create(title='Test Novel Beta')
    chapter_one_n1 = Chapter.objects.create(title='Chapter One', novel=novel, is_completed=True)
    chapter_two_n1 = Chapter.objects.create(title='Chapter Two', novel=novel)
    chapter_one_n2 = Chapter.objects.create(title='Chapter 1', novel=novel_two)
    novels_response = client.get('/api/novels/')
    first_novel = novels_response.data[0]
    first_novel_id = first_novel['client_id']
    novel_chapters_url = first_novel['chapters']
    chapters_response = client.get(novel_chapters_url)
    chapters_response_query = client.get('/api/chapters/?novel={}'.format(first_novel_id))
    assert len(chapters_response.data) == len(chapters_response_query.data)
    assert len(chapters_response.data) == 2
