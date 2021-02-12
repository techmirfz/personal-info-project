from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.basicinfoview, name='basicinfoview'),
    path('add/', views.basicinfoadd, name='basicinfoadd'),
    path('edit/', views.basicinfoedit, name='basicinfoedit'),
]
