from django.urls import path

from courses import views

urlpatterns = [
    path('student_courses/', views.StudentCoursesListView.as_view()),
]
