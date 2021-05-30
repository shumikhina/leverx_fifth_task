from django.urls import path
from rest_framework import routers

from courses import views

router = routers.SimpleRouter()
router.register(r'professor_courses', views.ProfessorCoursesViewSet, 'Professor_courses')

urlpatterns = [
    path('student_courses/', views.StudentCoursesListView.as_view()),
] + router.urls
