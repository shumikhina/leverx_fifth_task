from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db.models import Q

from homeworks.models import Homework, ReadyHomework
from lections.models import Lecture
from lections.serializers import LecturesSerializer


class HomeworkSerializer(serializers.ModelSerializer):
    lecture_id = serializers.IntegerField(write_only=True)
    lecture = LecturesSerializer(read_only=True)

    class Meta:
        model = Homework
        fields = ['pk', 'text', 'lecture', 'lecture_id']

    def validate(self, attrs):
        lecture_id = attrs.get('lecture_id')
        if lecture_id is not None:
            lecture = Lecture.objects.filter(
                Q(id=attrs['lecture_id']) &
                (
                    Q(course__owner=self.context['request'].user) |
                    Q(course__invited_professors=self.context['request'].user)
                )
            )
            if not lecture.exists():
                raise ValidationError('Can only use available lecture.')
            attrs['lecture'] = lecture.first()
        return attrs


class ReadyHomeworkSerializer(serializers.ModelSerializer):
    homework = HomeworkSerializer(read_only=True)
    homework_id = serializers.IntegerField(write_only=True)
    student = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = ReadyHomework
        fields = ['pk', 'homework', 'student', 'text', 'mark', 'comment', 'homework_id', 'student_comment']
        read_only_fields = ['mark', 'comment', 'student_comment']

    def validate(self, attrs):
        homework = Homework.objects.filter(
            Q(id=attrs['homework_id']) & Q(lecture__course__students=self.context['request'].user)
        )
        if not homework.exists():
            raise ValidationError('Can only use available homeworks.')
        attrs['homework'] = homework.first()
        return attrs


class ReadyHomeworkProfessorUpdateSerializer(serializers.ModelSerializer):
    homework = HomeworkSerializer(read_only=True)

    class Meta:
        model = ReadyHomework
        fields = ['pk', 'homework', 'student', 'text', 'mark', 'comment', 'student_comment']
        read_only_fields = ['pk', 'homework', 'student', 'text', 'student_comment']


class ReadyHomeworkStudentCommentUpdateSerializer(serializers.ModelSerializer):
    homework = HomeworkSerializer(read_only=True)

    class Meta:
        model = ReadyHomework
        fields = ['pk', 'homework', 'student', 'text', 'mark', 'comment', 'student_comment']
        read_only_fields = ['pk', 'homework', 'student', 'text', 'mark', 'comment']
