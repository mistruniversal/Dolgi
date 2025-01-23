from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)  # Поле заголовка
    content = models.TextField()  # Поле текста

    def __str__(self):
        return self.title  # Возвращаем заголовок для удобства

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя категории')  # Поле имени с удобочитаемым именем
    slug = models.SlugField(unique=True, verbose_name='Слаг - это часть URL-адреса ресурса')  # Уникальное поле адреса

    def __str__(self):
        return self.name  # Возвращаем имя категории для удобства

class Book(models.Model):
    title = models.CharField(max_length=200)  # Заголовок книги
    author = models.CharField(max_length=100)  # Автор книги
    published_date = models.DateField()  # Дата публикации
    isbn = models.CharField(max_length=13)  # ISBN книги

    def __str__(self):
        return self.title  # Возвращаем заголовок книги для удобства
