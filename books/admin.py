from django.contrib import admin
from books.models import (BookModel, PublisherModel, CategoryModel, BookLanguageModel, TranslatorModel, FeaturesModel,
                          AuthorModel, BookImageModel)


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'gender')
    list_display_links = ('name', 'last_name', 'gender')


@admin.register(PublisherModel)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(BookLanguageModel)
class BookLanguageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class BookImageStackedInline(admin.StackedInline):
    model = BookImageModel


@admin.register(TranslatorModel)
class TranslatorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',)
    list_display_links = ('id', 'first_name', 'last_name')


@admin.register(FeaturesModel)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'publisher')
    list_display_links = ('id', 'publisher')


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'real_price')
    list_display_links = ('book_name', 'real_price')
    inlines = [BookImageStackedInline]  # istagancha rasim qoshish imkonini beradi
    readonly_fields = ['stars', 'real_price', 'readed', 'reading', 'well_read']
