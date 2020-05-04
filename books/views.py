from django.shortcuts import render
# Create your views here.
from books.models import Book


def hello_world(request):
    return render(request, template_name="hello.html")


def prev_ex(request):
    return render(request, template_name="index.html")


def list_books(request):
    books = Book.objects.all()
    context = {
        "klucz": 123,
        "books": books,
    }
    return render(request, template_name="book_list.html", context=context)

