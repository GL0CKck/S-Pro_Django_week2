from django.urls import path

from .views import book_list, create_book, create_author, SearchBookView, BookDetailView

urlpatterns = [
    path('all_books/', book_list, name='book_list'),
    path('create_book/', create_book, name='created_book'),
    path('create_author/', create_author, name='created_book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('search_book/', SearchBookView.as_view(), name='search_book'),
]