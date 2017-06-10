from django import forms
from django.contrib.auth import authenticate


class AuthForm(forms.Form):
    """Basic authentication form. """
    username = forms.CharField(label='Логін', max_length=32)
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(),
                               max_length=32
                               )

    def authenticate(self):
        """Return User object or None. Form must be valid. """
        return authenticate(username=self.cleaned_data.get('username'),
                            password=self.cleaned_data.get('password')
                            )

class RegistrationForm(forms.Form):
    """Basic registration form."""
    pass
