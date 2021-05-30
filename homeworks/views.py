from rest_framework.generics import CreateAPIView

from authapp.permissions import ProfessorAllowed
from homeworks.serializers import HomeworkSerializer


class HomeworkAPIView(CreateAPIView):

    permission_classes = [ProfessorAllowed]
    serializer_class = HomeworkSerializer
