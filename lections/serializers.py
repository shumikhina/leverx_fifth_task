from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from courses.models import Course
from courses.serializers import CourseSerializer
from lections.models import Lecture


class LecturesSerializer(serializers.ModelSerializer):
    course_id = serializers.IntegerField(write_only=True)
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lecture
        fields = ['pk', 'course', 'presentation', 'course_id']

    def validate(self, attrs):
        course_id = attrs.get('course_id')
        if course_id is not None:
            course = Course.objects.filter(
                Q(id=attrs['course_id']) &
                (
                        Q(owner=self.context['request'].user) |
                        Q(invited_professors=self.context['request'].user)
                )
            )
            if not course.exists():
                raise ValidationError('Can only use available course.')
            attrs['course'] = course.first()
        return attrs
