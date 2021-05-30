from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

from authapp.permissions import ProfessorAllowed
from lections.models import Lecture
from lections.serializers import LecturesSerializer


class ProfessorLecturesViewSet(ModelViewSet):

    permission_classes = [ProfessorAllowed]
    serializer_class = LecturesSerializer

    def get_queryset(self):
        return Lecture.objects.filter(
            Q(course__owner=self.request.user) |
            Q(course__invited_professors=self.request.user)
        ).distinct()
