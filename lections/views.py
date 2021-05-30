from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from authapp.permissions import ProfessorAllowed, StudentAllowed
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


class StudentLectureListView(ListAPIView):

    permission_classes = [StudentAllowed]
    serializer_class = LecturesSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Lecture.objects.filter(
            Q(course__students=self.request.user) &
            Q(course_id=course_id)
        ).distinct()
