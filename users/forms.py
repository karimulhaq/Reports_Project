
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserSignupForm(UserCreationForm):
    email = forms.EmailField( required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
 


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields= ['username', 'password']

