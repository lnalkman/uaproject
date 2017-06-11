from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class AuthForm(forms.Form):
    """Basic authentication form. """
    username = forms.CharField(label='Логін', max_length=32)
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(),
                               max_length=128
                               )
                               

class RegistrationForm(forms.ModelForm):
    """Basic registration form."""
    password2 = forms.CharField(label='Повторіть пароль',
                               widget=forms.PasswordInput(),
                               max_length=128
                               )

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
