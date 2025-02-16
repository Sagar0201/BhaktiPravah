from django.urls import path
from bhakti import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.home, name='home'),
    
    path('info/<int:info_id>/', views.info, name='info'),
    path('categories/<str:category>/', views.categories, name='categories'),
    path('info_lists/<int:info_list_id>/', views.info_list_detail, name='info_list_detail'),
    path('counter', views.counter, name='counter'),

]
