__author__ = 'Greg Ziegan'
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class LinkHeaderPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        next_url = self.get_next_link()
        previous_url = self.get_previous_link()

        if next_url is not None and previous_url is not None:
            link = '<{next_url}>; rel="next", <{previous_url}>; rel="prev"'
        elif next_url is not None:
            link = '<{next_url}>; rel="next"'
        elif previous_url is not None:
            link = '<{previous_url}>; rel="prev"'
        else:
            link = ''

        link = link.format(next_url=next_url, previous_url=previous_url)
        headers = {'Link': link} if link else {}

        return Response(data, headers=headers)

class LargeResultsSetPagination(LinkHeaderPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StandardResultsSetPagination(LinkHeaderPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

