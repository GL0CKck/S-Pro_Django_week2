from django.urls import path

from .views import book_list, book_detail, author_detail

urlpatterns = [
    path('all_books/', book_list, name='book_list'),
    path('book/<int:index>/', book_detail, name='book_detail'),
    path('author_books/<int:index>/', author_detail, name='author_detail'),
]