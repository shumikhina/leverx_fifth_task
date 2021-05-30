from django.db.models import Q
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, ListCreateAPIView

from authapp.permissions import ProfessorAllowed, StudentAllowed
from homeworks.models import ReadyHomework, Homework
from homeworks.serializers import HomeworkSerializer, ReadyHomeworkSerializer, ReadyHomeworkProfessorUpdateSerializer, \
    ReadyHomeworkStudentCommentUpdateSerializer


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


class ReadyHomeworkProfessorUpdateView(UpdateAPIView):
    permission_classes = [ProfessorAllowed]
    serializer_class = ReadyHomeworkProfessorUpdateSerializer

    def get_queryset(self):
        return ReadyHomework.objects.filter(
            Q(homework__lecture__course__owner=self.request.user) |
            Q(homework__lecture__course__invited_professors=self.request.user)
        ).distinct()


class StudentHomeworksListView(ListAPIView):

    permission_classes = [StudentAllowed]
    serializer_class = HomeworkSerializer

    def get_queryset(self):
        lecture_id = self.kwargs['lecture_id']
        return Homework.objects.filter(
            Q(lecture__course__students=self.request.user) &
            Q(lecture_id=lecture_id)
        ).distinct()


class StudentReadyHomeworkListCreateView(ListCreateAPIView):

    permission_classes = [StudentAllowed]
    serializer_class = ReadyHomeworkSerializer

    def get_queryset(self):
        return ReadyHomework.objects.filter(
            Q(student=self.request.user)
        ).distinct()


class StudentReadyHomeworkUpdateCommentView(UpdateAPIView):

    permission_classes = [StudentAllowed]
    serializer_class = ReadyHomeworkStudentCommentUpdateSerializer

    def get_queryset(self):
        return ReadyHomework.objects.filter(
            Q(student=self.request.user)
        ).distinct()
