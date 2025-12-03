from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    copies = models.IntegerField(default=1)

    def __str__(self):
        return self.title


class BorrowedBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField(auto_now_add=True)



# Create your models here.
