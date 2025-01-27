from django.shortcuts import render
from .models import Category

def home(request):
    categories = Category.objects.all()

    return render(request, 'home.html',{'categories': categories})  # Render home.html template
