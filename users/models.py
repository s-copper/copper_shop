from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse


class MyUser(AbstractUser):
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:profile', args=[self.id])
