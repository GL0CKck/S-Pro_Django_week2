from django.contrib import admin

from .models import Author, Book, CommentUsers, Store

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(CommentUsers)
admin.site.register(Store)
