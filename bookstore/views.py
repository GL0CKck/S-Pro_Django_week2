from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
book_list_array = [
    {'id': 1, 'title': 'Fluent Python', 'released_data': 2005, 'description': 'Python’s simplicity lets you become productive quickly, '
                                                                              'but this often means you aren’t using everything it has to offer. '
                                                                              'With this hands-on guide, you’ll learn how to write effective, '
                                                                              'idiomatic Python code by leveraging its best—and possibly most n'
                                                                              'eglected—features. Author Luciano Ramalho takes you through Python’s core '
                                                                              'language features and libraries, and shows you how to make your code shorter, '
                                                                              'faster, and more readable at the same time.',
     'author_id': 1, 'author_name': 'Luciano Ramalho'},
    {'id': 2, 'title': 'Head First Python', 'released_data': 2010, 'description': 'Head First Python is a complete learning experience for Python that helps you learn '
                                                                              'the language through a unique method that goes beyond syntax and how-to manuals, helping '
                                                                              'you understand how to be a great Python programmer.',
     'author_id': 2, 'author_name': 'Paul Barry'},
    {'id': 3, 'title': 'Fluent Python', 'released_data': 2005, 'description': 'Python’s simplicity lets you become productive quickly, '
                                                                              'but this often means you aren’t using everything it has to offer. '
                                                                              'With this hands-on guide, you’ll learn how to write effective, '
                                                                              'idiomatic Python code by leveraging its best—and possibly most n'
                                                                              'eglected—features. Author Luciano Ramalho takes you through Python’s core '
                                                                              'language features and libraries, and shows you how to make your code shorter, '
                                                                              'faster, and more readable at the same time.',
     'author_id': 1, 'author_name': 'Luciano Ramalho'},
    {'id': 4, 'title': 'Head First Python', 'released_data': 2010, 'description': 'Head First Python is a complete learning experience for Python that helps you learn '
                                                                              'the language through a unique method that goes beyond syntax and how-to manuals, helping '
                                                                              'you understand how to be a great Python programmer.',
     'author_id': 2, 'author_name': 'Paul Barry'},
]


def book_list(request):
    books = [x for x in book_list_array]
    # book_l = ''.join(book)
    context = {'books': books}
    return render(request, 'all_books.html', context)


def book_detail(request, index):
    try:
        book = book_list_array[int(index) - 1]
        context = {'book': book}
        return render(request, 'book.html', context)

    except IndexError:
        return HttpResponse(f'Out of range index {index}')


def author_detail(request, index):
    try:
        books = [x for x in book_list_array if x['author_id'] == index]
        print(books)
        context = {'books': books}
        return render(request, 'author_book.html', context)

    except IndexError:
        return HttpResponse(f'Out of range index {index}')