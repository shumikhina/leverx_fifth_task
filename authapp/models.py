from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    STUDENT = 1
    PROFESSOR = 2
    ADMIN = 3

    ROLES = (
        (STUDENT, 'student'),
        (PROFESSOR, 'professor'),
        (ADMIN, 'admin'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLES)
