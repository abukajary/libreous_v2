from django import forms
from django.forms import ModelForm, PasswordInput, EmailInput, DateInput
from .models import AuthUser


class LoginForm(forms.Form):
    username = forms.CharField(label=u'User Name')
    password = forms.CharField(label=u'Password', widget=forms.PasswordInput(render_value=False))


class RegisterForm(ModelForm):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=PasswordInput)
    email = forms.CharField(widget=EmailInput)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = AuthUser
        fields = ["username", "password", "email", "first_name", "last_name"]
