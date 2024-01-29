from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import (BookModel, CategoryModel, BookImageModel, AuthorModel, BookLanguageModel,
                     BookCoverModel, PublisherModel)
from .serializers import BookSerializer, BookDetailSerializer, CategorySerializer, AuthorSerializer, \
    BookLanguageSerializer, BookCoverSerializer, PublisherSerializer


class BookCoverList(ListAPIView):
    queryset = BookCoverModel.objects.all()
    serializer_class = BookCoverSerializer


class PublisherList(ListAPIView):
    queryset = PublisherModel.objects.all()
    serializer_class = PublisherSerializer


class CategoryListView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


class AuthorListView(ListAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer


class BookLanguageListView(ListAPIView):
    queryset = BookLanguageModel.objects.all()
    serializer_class = BookLanguageSerializer


class BookListView(ListAPIView):
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()


class BookDetailView(RetrieveAPIView):
    serializer_class = BookDetailSerializer
    queryset = BookModel.objects.all()
