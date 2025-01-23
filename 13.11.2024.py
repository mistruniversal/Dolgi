from django.shortcuts import render
from django.template.response import TemplateResponse

# Задача 1
def index(request):
    return render(request, 'index.html')

# Задача 2
def index_template_response(request):
    return TemplateResponse(request, 'index.html')

# Задача 3
def contacts(request):
    data = 'Телефон: +79123456789, E-Mail: admin@email.com'
    return render(request, 'contacts.html', {'data': data})

# Задача 4
def profile(request):
    profile_data = {'name': 'Дмитрий', 'age': 39, 'phone': '+79123456789', 'email': 'dmitry@email.com'}
    return render(request, 'profile.html', profile_data)

# Задача 5
def profile_with_variable_name(request):
    profile_data = {'name': 'Дмитрий', 'age': 39, 'phone': '+79123456789', 'email': 'dmitry@email.com'}
    return render(request, 'profile.html', {'profile_data': profile_data})
