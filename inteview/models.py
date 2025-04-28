from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cabin_name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Department(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Subject(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()


from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name="ingredients", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    average_rating = models.FloatField()
    isbn = models.CharField(max_length=150)
    isbn13 = models.CharField(max_length=150)
    language_code = models.CharField(max_length=10)
    num_pages = models.IntegerField()
    rating_count = models.BigIntegerField()
    text_review_count = models.BigIntegerField()
    publication_date = models.DateField(auto_now=True)
    publisher = models.CharField(max_length=150)

    def __str__(self):
        return f" {self.title}  {self.authors}"
