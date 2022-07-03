from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.utils import timezone
from rest_framework.views import APIView

from .forms import BookForm, AuthorForm, CommentForm
from .models import Book, Store
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CreateStore

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


@api_view(['GET'])
def show_date(request):
    return Response({'Date:': timezone.now().date(),
                     'Year:': timezone.now().year,
                     'Month:': timezone.now().month,
                     'Day:': timezone.now().day})


@api_view(['GET'])
def hello_world(request):
    return Response({'msg': 'Hello Django REST!!'})


@api_view(['GET'])
def my_name(request, name):
    return Response({'Name': name})


@api_view(['POST'])
def calculate(request, num1, act, num2):
    if request.method == 'POST':
        action = {'plus': '+', 'minus': '-', 'mylti': '*', 'devide': '/'}
        if num2 != 0:
            raise ZeroDivisionError('Try divide on 0')
        if act in action:
            return Response({'num1 ': num1, 'action: ': action.get(act), 'num2: ': num2,
                             'result:': eval(num1 + action.get(act) + num2)})
        else:
            return Response('Your action not it our action')


class GetorCreateStore(APIView):
    serializer_class = CreateStore

    def get(self, request):
        store = Store.objects.all()
        serializer = CreateStore(store, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
