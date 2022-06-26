from django.forms import ModelForm

from .models import Book, Author, CommentUsers


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('full_name',)


class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'release_data', 'description']


class CommentForm(ModelForm):

    class Meta:
        model = CommentUsers
        fields = ['content']