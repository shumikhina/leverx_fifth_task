from django.urls import path

from homeworks import views

urlpatterns = [
    path('professor_homework/', views.HomeworkAPIView.as_view()),
]
