from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:profile', args=[self.id])


class UserAddress(models.Model):
    user = models.OneToOneField(MyUser)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    house_number = models.PositiveIntegerField(blank=True, null=True)
    building_number = models.PositiveIntegerField(blank=True, null=True)
    apartment = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
