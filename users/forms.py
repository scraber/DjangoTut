from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    display_name = forms.CharField(label="Display name")
    image = forms.ImageField(label="Profile picture", required=False)

    class Meta:
        model = User
        fields = [
            "username",
            "display_name",
            "image",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["email"]


class ProfileUpdateForm(forms.ModelForm):
    display_name = forms.CharField(label="Display name", required=False)
    image = forms.ImageField(label="Profile picture")

    class Meta:
        model = Profile
        fields = ["display_name", "image"]
