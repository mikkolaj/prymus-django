from django.shortcuts import render
# Create your views here.
from django.views.generic import ListView, DetailView

from books.models import Book, Author, Review
from django.contrib.auth.forms import UserCreationForm


def form(request):
    return render(request, template_name="form.html")


def title(request):
    return render(request, template_name="index.html")


def about(request):
    return render(request, template_name="about.html")


def prev_ex(request):
    return render(request, template_name="ex.html")


def list_books(request):
    books = Book.objects.all()
    context = {
        "klucz": 123,
        "books": books,
    }
    return render(request, template_name="books/book_list.html", context=context)


def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, template_name="books/book_details.html", context={'bookc': book})


class Bookdetails2(DetailView):
    model = Book
    template_name = "books/book_details.html"


def profile_view(request):
    return render(request, template_name="registration/profile.html")


def user_signup(request):
    if request.method == "POST":
        # przetwarzamy dane nowego użytkownika
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name="registration/signup_complete.html")
    else:
        # wyświetlamy czysty formularz
        form = UserCreationForm()
    return render(request, template_name="registration/signup_form.html", context={"form": form})


class AuthorList(ListView):
    model = Author
    template_name = "books/author_list.html"


class ReviewList(ListView):
    model = Review
    template_name = "books/review_list.html"


class AuthorDetail(DetailView):
    model = Author
    template_name = "books/author_detail.html"


class ReviewDetail(DetailView):
    model = Review
    template_name = "books/review_detail.html"

