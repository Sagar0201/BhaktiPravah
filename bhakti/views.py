from django.shortcuts import render
from .models import Category
from django.shortcuts import render, get_object_or_404
from .models import Information,InfoList,InfoListItem

    

def home(request):
    return render(request, 'home.html')  # Render home.html template


def homepage(request):
    # Get the search query from the GET request
    query = request.GET.get('query', '')

    # If there's a query, filter the Information objects
    if query:
        information_list = Information.objects.filter(
            heading__icontains=query  # Case-insensitive search on heading
        ).only('heading', 'id')
    else:
        information_list = Information.objects.only('heading', 'id')  # All information if no query

    categories = Category.objects.all()

    return render(request, 'homepage.html', {
        'information_list': information_list,
        'categories_data': categories,
        'query': query  # Pass the query back to the template for the search box
    })
    
    

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




def info_list_detail(request, info_list_id):
    print(info_list_id)
    info_list = InfoList.objects.get(id=info_list_id)  # Fetch the info list by ID
    information = InfoListItem.objects.filter(info_list=info_list)
    return render(request, 'info_list_detail.html', {'info_list': info_list, 'information': information})