from django.urls import path

from homeworks import views

urlpatterns = [
    path('professor_homeworks/', views.HomeworkCreateView.as_view()),
    path('professor_ready_homeworks/', views.ReadyHomeworkProfessorListView.as_view()),
    path('professor_ready_homeworks_update/<int:pk>/', views.ReadyHomeworkProfessorUpdateView.as_view()),

    path('student_homeworks_list/<int:lecture_id>/', views.StudentHomeworksListView.as_view()),
    path('student_add_homework/', views.StudentReadyHomeworkListCreateView.as_view()),
    path('student_update_homework_comment/<int:pk>/', views.StudentReadyHomeworkUpdateCommentView.as_view()),
]
