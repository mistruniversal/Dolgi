
from django.urls import path
from . import views

# Список маршрутов для товаров
product_patterns = [
    path('', views.products, name='products'),  # /products/
    path('new/', views.new, name='new_products'),  # /products/new/
    path('top/', views.top, name='top_products'),  # /products/top/
]

urlpatterns = [
    path('', views.index, name='index'),  # Корневая страница
    path('products/', include(product_patterns)),  # Включаем маршруты для товаров
]



from django.urls import path, include
from . import views

# Список маршрутов для товаров
product_patterns = [
    path('', views.products, name='product_detail'),  # /products/<id>/
    path('comments/', views.comments, name='product_comments'),  # /products/<id>/comments/
    path('questions/', views.questions, name='product_questions'),  # /products/<id>/questions/
]

urlpatterns = [
    path('', views.index, name='index'),  # Корневая страница
    path('products/<int:id>/', include(product_patterns)),  # Включаем маршруты для товаров с id
]





from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Корневая страница
    path('user/', views.user, name='user'),  # /user/?name=John&age=42
]







from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Корневая страница
    path('about/', views.about, name='about'),  # /about/
    path('contact/', views.contact, name='contact'),  # /contact/
    path('details/', views.details, name='details'),  # /details/
]
