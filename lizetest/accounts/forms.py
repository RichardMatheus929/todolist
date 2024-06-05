from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import User
from django.contrib.auth import password_validation


class CustomUserCreationForm(UserCreationForm):

    password1 = forms.CharField(
        label=("Senha"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "new-password", "id": "password1"}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=("Confirmação de senha"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","id":"password2"}),
        strip=False,
        help_text=('<strong id="aviso_text"></strong>'),
    )

    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
