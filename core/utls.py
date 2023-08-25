from django.core.paginator import InvalidPage
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# 分页
class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pageSize'
    page_query_param = 'page'
    max_page_size = 100

    def __init__(self):
        self.request = None
        self.page = None

    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate a queryset if required, either returning a
        page object, or `None` if pagination is not configured for this view.
        """
        page_size = self.get_page_size(request)
        if not page_size:
            return None

        paginator = self.django_paginator_class(queryset, page_size)
        page_number = self.get_page_number(request, paginator)

        try:
            # 正常翻页
            self.page = paginator.page(page_number)
            if paginator.num_pages > 1 and self.template is not None:
                # The browsable API should display pagination controls.
                self.display_page_controls = True
        except InvalidPage as exc:
            # 页码超出时
            self.page = self.django_paginator_class([], page_size).page("1")
            self.page.paginator.count = len(queryset)

        self.request = request
        return list(self.page)

    def get_paginated_response(self, data):
        return Response({
            'respCode': 200,
            'respMsg': '操作成功!',
            'data': {
                'page': int(self.request.query_params.get(self.page_query_param, 1)),
                'pageSize': self.get_page_size(self.request),
                'total': self.page.paginator.count,  # 重写翻页返回的字段
                # 'next': self.get_next_link(),
                # 'previous': self.get_previous_link(),
                'resource': data
            }
        })
