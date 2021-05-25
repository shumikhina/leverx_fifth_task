from django.db import models

from courses.models import Course


class Lecture(models.Model):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    presentation = models.FileField()
