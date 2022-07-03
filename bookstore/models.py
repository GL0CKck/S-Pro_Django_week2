from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=127, verbose_name='Name and Surname')

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=66, verbose_name='Title')
    author = models.ForeignKey(Author, auto_created=True, on_delete=models.CASCADE, verbose_name='Author')
    release_data = models.DateField(verbose_name='Release Data')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title


class CommentUsers(models.Model):
    content = models.TextField()
    owner_comment = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='my_comment')


class Store(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=800)
    rating = models.IntegerField(default=0, blank=True, null=True)