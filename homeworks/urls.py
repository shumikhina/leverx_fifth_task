from django.urls import path

from homeworks import views

urlpatterns = [
    path('professor_homeworks/', views.HomeworkCreateView.as_view()),
    path('professor_ready_homeworks/', views.ReadyHomeworkProfessorListView.as_view()),
]
