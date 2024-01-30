from rest_framework import serializers
from books.models import (BookModel, CategoryModel, BookImageModel, AuthorModel, BookLanguageModel,
                          PublisherModel, FeaturesModel)


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
        fields = ['full_name']


class BookImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImageModel
        fields = ['image']


class FeaturesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturesModel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return BookModel.objects.filter(category=obj).count()

    class Meta:
        model = CategoryModel
        fields = ['name', 'count']


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer()

    # author = serializers.SerializerMethodField()

    # def get_author(self, obj):
    #     author = AuthorModel.objects.filter(id=obj.id)
    #     return author

    class Meta:
        model = BookModel
        fields = ['id', 'main_image', 'authors', 'book_name', 'stars', 'price', 'real_price']


class BookModelDetailSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer()
    images = BookImageSerializer(many=True)
    features = FeaturesModelSerializer()

    class Meta:
        model = BookModel
        fields = '__all__'

# class BookDetailSerializer(serializers.ModelSerializer):
#     images = BookImageSerializer(many=True)
#     languages = BookLanguageSerializer()
#     publisher = PublisherSerializer()
#     authors = AuthorSerializer()
#
#     class Meta:
#         model = BookModel
#         exclude = ['category', 'created_at']
#         extra_fields = ['images']  # modelda image ga book teskari boglangan related name images
#         extra_fields qoshimcha fild qoshadi
