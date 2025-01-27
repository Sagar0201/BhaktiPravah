from django.contrib import admin
from .models import Category
from .models import Information

admin.site.register(Category)  # Register the Category model to the admin panel
admin.site.register(Information)  # Register the Information model to the admin panel
