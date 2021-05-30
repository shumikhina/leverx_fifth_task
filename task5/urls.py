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

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Task 5",
      default_version='v1',
      description="Task 5",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="do_not_to_contact_me@seriously.com"),
      license=openapi.License(name="Constitution"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('auth/', include(('authapp.urls', 'authapp'), namespace='authapp')),
    path('courses/', include(('courses.urls', 'courses'), namespace='courses')),
    path('lections/', include(('lections.urls', 'lections'), namespace='lections')),
    path('homeworks/', include(('homeworks.urls', 'homeworks'), namespace='homeworks')),
]
