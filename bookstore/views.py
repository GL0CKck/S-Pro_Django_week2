from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView
from django.shortcuts import get_object_or_404
from .forms import BookForm, AuthorForm
from .models import Author, Book


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('book_list')
        else:
            pass

    form = BookForm()
    context = {'form': form}
    return render(request, 'create_book.html', context)


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('book_list')
        else:
            pass

    form = AuthorForm()
    context = {'form': form}
    return render(request, 'create_book.html', context)


def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'all_books.html', context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    context = {'book': book}
    return render(request, 'book.html', context)


class SearchBookView(ListView):
    model = Book
    template_name = 'search_book.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(title__icontains=query)
        return object_list