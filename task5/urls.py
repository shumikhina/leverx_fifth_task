"""task5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('auth/', include(('authapp.urls', 'authapp'), namespace='authapp')),
    path('courses/', include(('courses.urls', 'courses'), namespace='courses')),
    path('lections/', include(('lections.urls', 'lections'), namespace='lections')),
    path('homeworks/', include(('homeworks.urls', 'homeworks'), namespace='homeworks')),
    path('ready_homeworks/', include(('homeworks.urls', 'homeworks'), namespace='ready_homeworks')),

]
