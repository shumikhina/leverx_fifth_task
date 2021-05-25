from django.db import models

from authapp.models import User


class Course(models.Model):

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)
    students = models.ManyToManyField(User, related_name='available_courses', related_query_name='available_courses')
    invited_professors = models.ManyToManyField(
        User, related_name='collaborated_courses', related_query_name='collaborated_courses'
    )
    owner = models.ForeignKey(User, related_name='owned_courses', on_delete=models.CASCADE)
