"""
authentication forms
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User



class CustomUserCreationForm(UserCreationForm):
    """
    Custom user creation form
    """
    class Meta(UserCreationForm):
        model = User
        fields = ('username',"profile_picture")


class CustomUserChangeForm(UserChangeForm):
    """
    Custom user change form
    """
    class Meta:
        model = User
        fields = ('username',"profile_picture")



class RegistrationForm(CustomUserCreationForm):
    """
    registration form
    """

    class Meta:
        model = User
        fields = ("username", "profile_picture","password1", "password2", )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        if commit:
            user.save()
        return user