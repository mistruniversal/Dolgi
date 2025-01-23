
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')





from django.shortcuts import render
from django.template.response import TemplateResponse

def index(request):
    return TemplateResponse(request, 'index.html')




from django.shortcuts import render

def contacts(request):
    data = 'Телефон: +79123456789, E-Mail: admin@email.com'
    context = {'data': data}
    return render(request, 'contacts.html', context)





from django.shortcuts import render

def profile(request):
    context = {
        'name': 'Дмитрий',
        'age': 39,
        'phone': '+79123456789',
        'email': 'dmitry@email.com'
    }
    return render(request, 'profile.html', context)
