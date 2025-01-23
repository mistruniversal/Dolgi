from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)  # Поле заголовка
    content = models.TextField()  # Поле текста

    def __str__(self):
        return self.title  # Возвращаем заголовок при выводе объекта



from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя категории')  # Поле имени с удобочитаемым именем
    slug = models.SlugField(unique=True, help_text='Слаг - это часть URL-адреса ресурса')  # Поле адреса

    def __str__(self):
        return self.name  # Возвращаем имя категории при выводе объекта






from django.db import models
from django.utils import timezone

class Classroom(models.Model):
    name = models.CharField(max_length=50)  # Поле имени
    code = models.CharField(max_length=11, unique=True)  # Поле кода класса с уникальными значениями
    description = models.TextField(blank=True, default='')  # Поле описания, может быть пустым
    created = models.DateTimeField(auto_now_add=True)  # Дата и время создания
    updated = models.DateTimeField(auto_now=True)  # Дата и время обновления

    def __str__(self):
        return self.name  # Возвращаем имя класса при выводе объекта


