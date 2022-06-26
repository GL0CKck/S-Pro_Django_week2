from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import get_object_or_404
from django.views.generic.edit import FormMixin

from .forms import BookForm, AuthorForm, CommentForm
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


class SearchBookView(ListView):
    model = Book
    template_name = 'search_book.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(title__icontains=query)
        return object_list


class BookDetailView(DetailView, FormMixin, SuccessMessageMixin):
    model = Book
    template_name = 'book.html'
    context_object_name = 'get_book'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid:
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner_comment = self.request.user
        self.object.book = self.get_object()
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.get_object().id})
