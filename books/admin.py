from django.contrib import admin
from books.models import (BookModel, PublisherModel, CategoryModel, BookCoverModel, BookLanguageModel,
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
    list_display = ('name', 'count')
    list_display_links = ('name', 'count')
    readonly_fields = ['count']


@admin.register(BookCoverModel)
class BookCoverAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(BookLanguageModel)
class BookLanguageModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class BookImageStackedInline(admin.StackedInline):
    model = BookImageModel


@admin.register(BookModel)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'real_price')
    list_display_links = ('book_name', 'real_price')
    inlines = [BookImageStackedInline]  # istagancha rasim qoshish imkonini beradi
    readonly_fields = ['stars', 'real_price', 'readed', 'reading', 'well_read']
