from django.urls import path
from . import views

urlpatterns = [
	path('view/', views.assignmentview, name='assignmentview'),
	path('add', views.assignmentadd, name='assignmentadd'),
    path('edit/<int:pk>', views.assignmentedit, name='assignmentedit'),
]