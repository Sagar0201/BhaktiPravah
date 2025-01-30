from django.shortcuts import render
from .models import Category
from django.shortcuts import render, get_object_or_404
from .models import Information

def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html',{'categories': categories})  # Render home.html template


def homepage(request):
    information_list = Information.objects.only('heading', 'image','id')  
    return render(request, 'homepage.html',{'information_list': information_list})


def info(request,info_id):
    information = get_object_or_404(Information, id=info_id)
    return render(request, 'info.html', {'information': information})


def counter(request):
    return render(request, 'counter.html')