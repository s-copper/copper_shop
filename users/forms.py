from django.forms import ModelForm
from .models import MyUser


class UserCreateForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password', 'first_name', 'last_name', 'birthday']

