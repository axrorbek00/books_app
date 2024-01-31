from rest_framework.pagination import PageNumberPagination


class BooksPagination(PageNumberPagination):
    page_size = 1  # nechtadan chiqishi
    page_size_query_param = 'page_size'
    max_page_size = 1000
