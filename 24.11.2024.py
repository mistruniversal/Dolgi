from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()




class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя категории")
    slug = models.SlugField(unique=True, verbose_name="Слаг - это часть URL-адреса ресурса")




class Classroom(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=11, unique=True)
    description = models.TextField(blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  # Возвращаем имя класса







class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название записи")
    slug = models.SlugField(unique=True, max_length=80, verbose_name="URL")
    description = models.TextField(verbose_name="Краткое описание")
    text = models.TextField(verbose_name="Полный текст записи")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время добавления")
    updated = models.DateTimeField(auto_now=True, verbose_name="Время обновления")
    fixed = models.BooleanField(default=False, verbose_name="Прикреплено")
    class Meta:
        ordering = ['-created']
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
