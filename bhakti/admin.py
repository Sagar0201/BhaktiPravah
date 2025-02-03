from django.contrib import admin
from .models import Category
from .models import Information
from .models import Title
from .models import InfoList

admin.site.register(Category) 
admin.site.register(Title) 

admin.site.register(Information)
admin.site.register(InfoList)