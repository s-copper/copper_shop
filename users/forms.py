from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, DateInput
from .models import MyUser


class UserCreateForm(ModelForm):

    class Meta:
        model = MyUser
        fields = ['username', 'password', 'first_name', 'last_name', 'birthday']
        widgets = {
            'password': PasswordInput,
            'birthday': DateInput(attrs={'type': 'date'}),
        }
