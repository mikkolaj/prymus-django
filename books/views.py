from django.shortcuts import render
# Create your views here.
from books.models import Book
from django.contrib.auth.forms import UserCreationForm


def form(request):
    return render(request, template_name="form.html")


def title(request):
    return render(request, template_name="index.html")


def prev_ex(request):
    return render(request, template_name="ex.html")


def list_books(request):
    books = Book.objects.all()
    context = {
        "klucz": 123,
        "books": books,
    }
    return render(request, template_name="book_list.html", context=context)


def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, template_name="book_details.html", context={'bookc': book})


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
