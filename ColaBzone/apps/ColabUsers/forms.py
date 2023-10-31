from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from ..ColabUsers.models import ColabUser


class ColabUserCreationForm(UserCreationForm):
    class Meta:
        model = ColabUser
        fields = ("email", "password")


class ColabUserChangeForm(UserChangeForm):
    class Meta:
        model = ColabUser
        fields = ("email", "password")
