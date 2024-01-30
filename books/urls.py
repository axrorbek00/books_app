from django.urls import path
from .views import BookListView, BookDetailAPIView, CategoryDetailView

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
    path('books/cat/<int:pk>/', CategoryDetailView.as_view()),
]
