from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from authapp.permissions import StudentAllowed, ProfessorAllowed
from courses.models import Course
from courses.serializers import CourseSerializer


class StudentCoursesListView(ListAPIView):

    permission_classes = [StudentAllowed]
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(students=self.request.user)


class ProfessorCoursesViewSet(ModelViewSet):

    permission_classes = [ProfessorAllowed]
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(
            Q(owner=self.request.user) |
            Q(invited_professors=self.request.user)
        ).distinct()
