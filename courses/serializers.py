from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from authapp.models import User
from courses.models import Course


class StudentIdSerializer(serializers.Serializer):

    id = serializers.IntegerField()

    def validate(self, attrs):
        pk = attrs['id']
        if not User.objects.filter(pk=pk, role=User.STUDENT).exists():
            raise ValidationError('Allow to add only students.')
        return attrs


class ProfessorIdSerializer(serializers.Serializer):

    id = serializers.IntegerField()

    def validate(self, attrs):
        pk = attrs['id']
        if not User.objects.filter(pk=pk, role=User.PROFESSOR).exists():
            raise ValidationError('Allow to add only professors.')
        return attrs


class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    students = StudentIdSerializer(many=True, required=False)
    invited_professors = ProfessorIdSerializer(many=True, required=False)

    class Meta:
        model = Course
        fields = ['pk', 'name', 'description', 'owner', 'students', 'invited_professors']
        read_only_fields = ('pk', )

    @staticmethod
    def _get_related_instances(ids_map):
        return User.objects.filter(id__in=[item['id'] for item in ids_map])

    def create(self, validated_data):
        students = self._get_related_instances(validated_data.pop('students', []))
        professors = self._get_related_instances(validated_data.pop('invited_professors', []))
        course = Course.objects.create(
            name=validated_data['name'],
            description=validated_data['description'],
            owner=validated_data['owner']
        )
        course.invited_professors.set(professors)
        course.students.set(students)
        return course

    def update(self, instance, validated_data):
        students = self._get_related_instances(validated_data.pop('students', []))
        professors = self._get_related_instances(validated_data.pop('invited_professors', []))
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        instance.invited_professors.set(professors)
        instance.students.set(students)
        return instance
