from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLES = (
        (1, 'student'),
        (2, 'professor'),
        (3, 'admin'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLES)
