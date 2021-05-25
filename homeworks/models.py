from django.db import models

from authapp.models import User
from lections.models import Lecture


class Homework(models.Model):

    text = models.TextField()
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)


class ReadyHomework(models.Model):

    homework = models.ForeignKey(Homework, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    mark = models.IntegerField()
    comment = models.CharField(max_length=512)
