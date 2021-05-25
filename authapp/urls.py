from django.urls import path
from rest_framework.authtoken import views as rest_views

from authapp.views import RegistrationAPIView

urlpatterns = [
    path('log_in/', rest_views.obtain_auth_token),
    path('register/', RegistrationAPIView.as_view()),
]
