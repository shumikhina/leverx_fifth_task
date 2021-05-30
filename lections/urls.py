from rest_framework import routers

from lections import views

router = routers.SimpleRouter()
router.register(r'professor_lectures', views.ProfessorLecturesViewSet, 'Professor_lectures')

urlpatterns = [] + router.urls
