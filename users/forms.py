from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.forms.widgets import PasswordInput, DateInput
from .models import MyUser, UserAddress


class UserCreateForm(forms.ModelForm):

    password2 = forms.CharField(widget=forms.PasswordInput(), label="Повторите пароль")

    class Meta:
        model = MyUser
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name', 'birthday']
        widgets = {
            'password': PasswordInput,
            'birthday': DateInput(attrs={'type': 'date'}),
        }
        help_texts = {
            'username': 'Используйте латинские буквы, цифры и символы "@ . + - _"',
        }

    def clean_password(self):
        if self.data['password'] != self.data['password2']:
            raise forms.ValidationError('Passwords are not the same')
        return self.data['password']


class UserAddressForm(forms.ModelForm):

    class Meta:
        model = UserAddress
        fields = ['city', 'street', 'house_number', 'building_number', 'apartment']

    def clean(self):
        if any(self.cleaned_data.values()) and (not self.cleaned_data['city'] or not self.cleaned_data['house_number']):
            raise forms.ValidationError(
                message='Для сохранения адреса, поля "Город" и "Номер дома" не могут быть пустыми'
            )
        return self.cleaned_data


class UserEditForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'birthday']
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}),
        }


class UserChangePassword(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput(), label="Старый пароль")
    new_password1 = forms.CharField(widget=forms.PasswordInput(), label="Новый пароль")
    new_password2 = forms.CharField(widget=forms.PasswordInput(), label="Повторите новый пароль")

    class Meta:
        model = MyUser
        fields = ['old_password', 'new_password1', 'new_password2']

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.instance.check_password(old_password):
            raise forms.ValidationError(
                message='Неправильно введен пароль'
            )
        return old_password

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(message='Пароли не совпадают')
        return self.cleaned_data['new_password2']


class UserChangeEmail(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['email']
