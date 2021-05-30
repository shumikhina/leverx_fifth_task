from django.db.models import Q
from rest_framework.generics import CreateAPIView, ListAPIView

from authapp.permissions import ProfessorAllowed
from homeworks.models import ReadyHomework
from homeworks.serializers import HomeworkSerializer, ReadyHomeworkSerializer


class HomeworkCreateView(CreateAPIView):

    permission_classes = [ProfessorAllowed]
    serializer_class = HomeworkSerializer


class ReadyHomeworkProfessorListView(ListAPIView):

    permission_classes = [ProfessorAllowed]
    serializer_class = ReadyHomeworkSerializer

    def get_queryset(self):
        return ReadyHomework.objects.filter(
            Q(homework__lecture__course__owner=self.request.user) |
            Q(homework__lecture__course__invited_professors=self.request.user)
        ).distinct()
