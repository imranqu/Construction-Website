from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import form
from django import forms
from django.forms import ModelForm
from .models import profile
class Signup(UserCreationForm):
    print("hii from form")
    class Meta:
        fields=('username','email','password1','password2','first_name','last_name')
        model=get_user_model()


class EditProfile(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields=('first_name','last_name','username','email')



class ProfileForm(forms.ModelForm):

    class Meta:
        model = profile
        fields=['phone_number','address']


class Form(forms.ModelForm):
    class Meta:
        model= form
        fields=[
            'name','email','phone_number','address'
        ]
