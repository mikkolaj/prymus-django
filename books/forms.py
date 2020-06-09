from django import forms

from books.models import Book, Author, Review


class SimpleForm(forms.Form):
    name = forms.CharField(label="Jak masz na imie?", required=True)
    template_name = "books/simple_form.html"


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = []


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = []


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = []

