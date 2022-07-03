from django.urls import path

from .views import book_list, create_book, create_author, SearchBookView, BookDetailView, show_date, \
    my_name, hello_world, calculate, GetorCreateStore

urlpatterns = [
    path('all_books/', book_list, name='book_list'),
    path('create_book/', create_book, name='created_book'),
    path('create_author/', create_author, name='created_book'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('search_book/', SearchBookView.as_view(), name='search_book'),
    path('today/', show_date, name='show date'),
    path('my_name/<str:name>/', my_name, name='my name'),
    path('hello-django/', hello_world, name='hello world'),
    path('calculate/<str:num1>/<str:act>/<str:num2>/', calculate, name='calculate'),
    path('store/', GetorCreateStore.as_view(), name='get store'),
]