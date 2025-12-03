from django.shortcuts import render, redirect
from .models import Student, Book, BorrowedBook
from django.contrib import messages

def login_view(request):
    msg = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(username=username, password=password)
            request.session["student_id"] = student.id
            return redirect("dashboard")
        except Student.DoesNotExist:
            msg = "Invalid username or password"

    return render(request, "myproject/login.html", {"msg": msg})

def dashboard_view(request):
    if "student_id" not in request.session:
        return redirect("login")

    return render(request, "myproject/dashboard.html")

def books(request):
    return render(request, "myproject/books.html")

def borrow_book(request, book_id):
    return render(request, "myproject/borrow_success.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if Student.objects.filter(username=username).exists():
            return render(request, "myproject/register.html", {
                "msg": "Username already exists!"
            })

        Student.objects.create(username=username, password=password)
        return redirect("login")

    return render(request, "myproject/register.html")


