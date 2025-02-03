from django.shortcuts import render
from .models import Category
from django.shortcuts import render, get_object_or_404
from .models import Information
import threading
import requests


def can_not_stop():
    threading.Timer(1 * 60, my_function).start()
    requests.get("https://bhaktipravah.onrender.com/")
    
    
    

def home(request):
    return render(request, 'home.html')  # Render home.html template


def homepage(request):
    information_list = Information.objects.only('heading','id')  
    categories = Category.objects.all()
    can_not_stop()
    return render(request, 'homepage.html',{'information_list': information_list,'categories_data': categories})


def info(request,info_id):
    information = get_object_or_404(Information, id=info_id)
    return render(request, 'info.html', {'information': information})


def counter(request):
    return render(request, 'counter.html')


def categories(request,category):
    information_list = Information.objects.filter(category__category_name=category).only('heading', 'id')
    categories = Category.objects.all()
        # Separate selected category
    selected_category = categories.filter(category_name=category).first()
    other_categories = categories.exclude(category_name=category)

    # Combine selected category first, then others
    categories = [selected_category] + list(other_categories) if selected_category else list(categories)

    return render(request,'categories.html',{'information_list': information_list,'categories_data': categories,'category': category})