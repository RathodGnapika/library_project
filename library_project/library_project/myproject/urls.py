from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("books/", views.books, name="books"),
    path("borrow/<int:book_id>/", views.borrow_book, name="borrow_book"),
    path("register/", views.register_view, name="register"),
]
