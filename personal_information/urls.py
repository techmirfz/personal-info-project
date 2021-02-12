"""personal_information URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from basic_info import views as basic_info_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', basic_info_views.home, name='home'),

    # user authentication
    path('signup/', basic_info_views.signupuser, name='signupuser'),
    path('login/', basic_info_views.loginuser, name='loginuser'),
    path('logout/', basic_info_views.logoutuser, name='logoutuser'),

    #profile
    path('basicinfo/', include('basic_info.urls')),
 
    #training
    path('training/', include('training.urls')),

    #assignment
    #training
    path('assignment/', include('assignment.urls')),
]
