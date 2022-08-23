from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import MemberProfile


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = MemberProfile
        fields = ['username', 'age','password1', 'password2',\
            'img','email','first_name','last_name']
        labels = {
            "username": "Username",
            "password1": "Password",
            "password2": "Password confirmation",
            "age":"Age",
            "img": "Profile photo",
            "email":"Email",
            "first_name":"First name",
            "last_name":"Last name"
        }


class StaffCreationForm(UserCreationForm):
    
    class Meta:
        model = MemberProfile
        fields = ['username','password1', 'password2',\
            'img','email','first_name','last_name']
        labels = {
            "username": "Username",
            "password1": "Password",
            "password2": "Password confirmation",
            "img": "Profile photo",
            "email":"Email",
            "first_name":"First name",
            "last_name":"Last name"
        }
        

class MemberProfileForm(forms.ModelForm):
    
    class Meta:
        model = MemberProfile
        fields = ['username', 'first_name', 'last_name', 'age', 'img']
        labels = {
            "username": "Username",
            "first_name": "First name",
            "last_name": "Last name",
            "age":"Age",
            "img":"User Image"

        }        

    def __init__(self, *args, **kwargs):
        super(MemberProfileForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True