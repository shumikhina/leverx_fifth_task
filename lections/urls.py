from django.urls import path
from rest_framework import routers

from lections import views

router = routers.SimpleRouter()
router.register(r'professor_lectures', views.ProfessorLecturesViewSet, 'Professor_lectures')

urlpatterns = [
    path('student_lectures/<int:course_id>/', views.StudentLectureListView.as_view()),
] + router.urls
