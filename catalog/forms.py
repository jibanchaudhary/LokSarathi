from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms import PasswordInput,TextInput,ModelForm

from .models import *

# Creating Signup(Model form)
class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())

# For the admin to CRUD
class addQuestionform(ModelForm):
    class Meta:
        model=MCQmodel
        fields=['question','option1','option2','option3','option4','correct_option']



