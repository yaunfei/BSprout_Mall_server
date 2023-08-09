from rest_framework.pagination import PageNumberPagination


# 分页
class Pagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'pageSize'
    page_query_param = 'page'
    max_page_size = 100
