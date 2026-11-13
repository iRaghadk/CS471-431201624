from django.db import models
from django.db.models import Sum

# Lab 9 Models
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    pubdate = models.DateTimeField()
    rating = models.SmallIntegerField(default=1)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

    @property
    def availability_percentage(self):
        total_quantity = Book.objects.aggregate(sum_qty=Sum('quantity'))['sum_qty']
        if total_quantity and total_quantity > 0:
            return round((self.quantity / total_quantity) * 100, 2)
        return 0

# --- Lab 8 & Lab 11 - Task 1: One-to-Many Models ---
class Address(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# --- Lab 11 - Task 2: Many-to-Many Models ---
class Address2(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    addresses = models.ManyToManyField(Address2)

    def __str__(self):
        return self.name

# --- Lab 11 - Task 3: Image Upload Model ---
class BookPhoto(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_photos/')

    def __str__(self):
        return self.title