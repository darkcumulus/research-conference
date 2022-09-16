from django import forms
from django.forms import EmailField

from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LogoutForm(forms.Form):
    pass


class UserCreationForm(UserCreationForm):
    email = EmailField(
        label=_("Email address"), required=True, help_text=_("Required.")
    )
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
