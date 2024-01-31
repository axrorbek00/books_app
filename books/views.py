from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import (BookModel, CategoryModel, BookImageModel, AuthorModel, BookLanguageModel,
                     PublisherModel)
from .paginations import BooksPagination
from .serializers import BookSerializer, CategorySerializer, AuthorSerializer, \
    BookLanguageSerializer, PublisherSerializer, BookModelDetailSerializer
from rest_framework import filters


class CategoryListView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    pagination_class = None


class AuthorListView(ListAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer


class CategoryDetailView(APIView):

    def get(self, request, pk, *args, **kwargs):
        qs = BookModel.objects.filter(category_id=pk)
        serializer = BookSerializer(qs, many=True)
        return Response(serializer.data)


class BookListView(ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ('book_name',)
    pagination_class = BooksPagination

    # def list(self, request, *args, **kwargs):
    #     queryset = BookModel.objects.all()
    #     cat_qs = CategoryModel.objects.all()
    #     serializer = BookSerializer(queryset, many=True)
    #     cat_serializer = CategorySerializer(cat_qs, many=True)
    #     return Response({
    #         "books": serializer.data,
    #         "cats": cat_serializer.data
    #     })


class BookDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = BookModelDetailSerializer
    queryset = BookModel.objects.all()
