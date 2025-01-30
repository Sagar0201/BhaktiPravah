from django.urls import path
from bhakti import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.home, name='home'),
    
    path('info/<int:info_id>/', views.info, name='info'),
]
