from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    display_name = forms.CharField(label='Display name')
    image = forms.ImageField(label='Profile picture', required=False)

    class Meta:
        model = User
        fields = ['username', 'display_name', 'image',
                  'email', 'password1', 'password2']
