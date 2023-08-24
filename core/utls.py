from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# 分页
class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'pageSize'
    page_query_param = 'page'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'respCode': 200,
            'respMsg': '操作成功!',
            'data': {
                'page': self.request.query_params.get(self.page_query_param, 1),
                'pageSize': self.get_page_size(self.request),
                'total': self.page.paginator.count,  # 重写翻页返回的字段
                # 'next': self.get_next_link(),
                # 'previous': self.get_previous_link(),
                'resource': data
            }

        })
