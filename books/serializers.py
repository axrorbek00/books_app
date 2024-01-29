from rest_framework import serializers
from books.models import (BookModel, CategoryModel, BookImageModel, AuthorModel, BookLanguageModel,
                          BookCoverModel, PublisherModel)


class BookCoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCoverModel
        fields = '__all__'


class BookLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLanguageModel
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherModel
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = '__all__'


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImageModel
        fields = ['image']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ['id', 'main_image', 'book_name', 'authors', 'stars', 'real_price']


class BookDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = BookImageSerializer(many=True)
    languages = BookLanguageSerializer()
    publisher = PublisherSerializer()
    book_cover = BookCoverSerializer()
    authors = AuthorSerializer()

    class Meta:
        model = BookModel
        fields = '__all__'
        extra_fields = ['images']  # modelda image ga book teskari boglangan related name images
        # extra_fields qoshimcha fild qoshadi
