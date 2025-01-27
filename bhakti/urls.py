from django.urls import path
from bhakti import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page route
]
