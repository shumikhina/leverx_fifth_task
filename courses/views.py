from rest_framework.generics import ListAPIView

from authapp.permissions import StudentAllowed
from courses.models import Course
from courses.serializers import CourseSerializer


class StudentCoursesListView(ListAPIView):

    serializer_class = CourseSerializer
    permission_classes = [StudentAllowed]

    def get_queryset(self):
        return Course.objects.filter(students=self.request.user)
