from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    birthday = models.DateField(blank=True, null=True, verbose_name='День рождения')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:profile', args=[self.id])


class UserAddress(models.Model):
    user = models.OneToOneField(MyUser)
    city = models.CharField(max_length=100, blank=True, verbose_name='Город')
    street = models.CharField(max_length=100, blank=True, verbose_name='Улица')
    house_number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер дома')
    building_number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Корпус')
    apartment = models.PositiveIntegerField(blank=True, null=True, verbose_name='Квартира')
    country = models.CharField(max_length=100, blank=True, verbose_name='Страна')
