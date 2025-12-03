from django.db import models

# -----------------------
# Student Model
# -----------------------
class Student(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# -----------------------
# Book Model
# -----------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title


# -----------------------
# Borrowed Book Model
# -----------------------
class BorrowedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} borrowed {self.book.title}"

