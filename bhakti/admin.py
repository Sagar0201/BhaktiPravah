from django.contrib import admin
from .models import Category
from .models import Information
from .models import Title
from .models import InfoList
from .models import InfoListItem

admin.site.register(Category) 
admin.site.register(Title) 

admin.site.register(Information)
admin.site.register(InfoList)
admin.site.register(InfoListItem)