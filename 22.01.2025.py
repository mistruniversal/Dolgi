from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=200, label='Заголовок')
    content = forms.CharField(widget=forms.Textarea, label='Контент')


class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100, label='Имя')
    age = forms.IntegerField(label='Возраст')
    about = forms.CharField(widget=forms.Textarea, label='О пользователе')
    email = forms.EmailField(label='E-Mail адрес')


class ProductForm(forms.Form):
    name = forms.CharField(max_length=50, label='Название продукта')
    description = forms.CharField(max_length=255, widget=forms.Textarea, label='Описание продукта')
    price = forms.IntegerField(label='Цена продукта')
