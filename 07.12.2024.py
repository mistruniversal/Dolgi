1
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


2
class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title




3
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=255)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_topics')

    def __str__(self):
        return self.title


4
class Genre(models.Model):
    name = models.CharField(max_length=200, verbose_name="Введите жанр книги")

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_death = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=255, verbose_name="Введите описание книги")
    isbn = models.CharField(max_length=13, verbose_name="Введите код ISBN")
    genre = models.ManyToManyField(Genre, verbose_name="Введите жанр книги")
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


