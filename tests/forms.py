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
    # password = forms.CharField(label='Пароль',
    #                            widget=forms.PasswordInput(),
    #                            max_length=128
    #                            )
    password2 = forms.CharField(label='Повторіть пароль',
                               widget=forms.PasswordInput(),
                               max_length=128
                               )

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


    def __init__(self, *args, **kwargs):
        base_init = super(forms.ModelForm, self).__init__(*args, **kwargs)

        # Bad localization
        self.fields['password'].widget = forms.PasswordInput()
        self.fields['password'].label = 'Пароль'                                            
        self.fields['email'].label = 'Емейл'
        self.fields['username'].label = 'Логін'

        return base_init


    def is_valid(self):
        if super(forms.ModelForm, self).is_valid():
            if self.cleaned_data['password'] == self.cleaned_data['password2']:
                return True
            self.add_error(None, 'Паролі не співпадають')

        return False
