from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response

from django_image_app_api.settings import REST_FRAMEWORK


class CustomPagination(pagination.PageNumberPagination):
    page_size = REST_FRAMEWORK['PAGE_SIZE']

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('count', self.page.paginator.count),
            ('page', self.page_size),
            ('num_page', self.page.paginator.num_pages),
            ('results', data),
        ]))
