from django.urls import path
from . import views

urlpatterns = [
	path('view/', views.trainingview, name='trainingview'),
	path('add', views.trainingadd, name='trainingadd'),
    path('edit/<int:pk>', views.trainingedit, name='trainingedit'),
]
