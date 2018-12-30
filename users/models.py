from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username
