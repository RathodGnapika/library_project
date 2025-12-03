from django.shortcuts import render, redirect
from .models import Student, Book, BorrowedBook
from .forms import LoginForm

def login_view(request):
    msg = ""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            student = Student.objects.get(username=username, password=password)
            request.session["student_id"] = student.id
            return redirect("dashboard")
        except:
            msg = "Invalid credentials!"

    return render(request, "portal/login.html", {"msg": msg})


def dashboard(request):
    student_id = request.session.get("student_id")
    if not student_id:
        return redirect("login")

    student = Student.objects.get(id=student_id)
    borrowed = BorrowedBook.objects.filter(student=student)

    return render(request, "portal/dashboard.html", {"student": student, "borrowed": borrowed})


def books(request):
    student_id = request.session.get("student_id")
    if not student_id:
        return redirect("login")

    all_books = Book.objects.all()
    return render(request, "portal/books.html", {"books": all_books})


def borrow_book(request, book_id):
    student_id = request.session.get("student_id")
    if not student_id:
        return redirect("login")

    student = Student.objects.get(id=student_id)
    book = Book.objects.get(id=book_id)

    if book.copies > 0:
        BorrowedBook.objects.create(student=student, book=book)
        book.copies -= 1
        book.save()
        return render(request, "portal/borrow_success.html", {"book": book})

    return render(request, "portal/borrow_success.html", {"book": None})


# Create your views here.
