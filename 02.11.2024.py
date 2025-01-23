
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Корневая страница
]




from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Корневая страница
    path('catalog/', views.catalog, name='catalog'),  # Страница каталога
    path('contact/', views.contact, name='contact'),  # Страница контактов
]









from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Корневая страница
    path('accounts/<str:name>/', views.accounts, name='accounts'),  # Страница аккаунтов с именем пользователя
]











from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Корневая страница
    path('accounts/<str:name>/<int:age>/', views.accounts, name='accounts_with_age'),  # Страница аккаунтов с именем и возрастом
    path('accounts/<str:name>/', views.accounts, name='accounts_with_name'),  # Страница аккаунтов с именем без возраста
    path('accounts/', views.accounts, name='accounts_default'),  # Страница аккаунтов по умолчанию
]
