"""libraryproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from books import views
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # <-- nowe
    path('admin/', admin.site.urls),
    path('accounts/signup/', views.user_signup, name="user_signup"),

    path('', views.title, name="title"),
    path('form/', views.form, name="form"),
    path('ex/', views.prev_ex, name="dawne"),
    path('about/', views.about, name="about"),

    path('ksiazki/', views.list_books, name='lista'),
    path("ksiazki/<int:pk>", views.Bookdetails2.as_view(), name='book_details'),
    path("ksiazki/dodaj", views.BookCreate.as_view(), name="book_create"),

    path("autorzy", views.AuthorList.as_view(), name="author_list"),
    path("autorzy/<int:pk>", views.AuthorDetail.as_view(), name="author_detail"),
    path("autorzy/dodaj", views.AuthorCreate.as_view(), name="author_create"),

    path("recenzje", views.ReviewList.as_view(), name="review_list"),
    path("recenzje/<int:pk>", views.ReviewDetail.as_view(), name="review_details"),
    path("recenzje/dodaj", views.ReviewCreate.as_view(), name="review_create"),

    path("formularz", views.SimpleFormView.as_view()),
    path("wyszukiwanie", views.search, name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
