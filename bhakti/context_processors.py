# bhakti/context_processors.py
from .models import Category
from .models import InfoList

def categories(request):
     return {'categories': Category.objects.all()}

# View to list all info lists
def info_lists(request):
     return {'info_lists': InfoList.objects.all() }
