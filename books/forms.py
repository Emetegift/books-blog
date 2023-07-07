# To create a blueprint for the registration form
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm): #This is the form class

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:  # This simply means the definition of class
        model = User
        fields = ['username', 'email', 'password'] #These are the fiels that are required of a user
        
class LoginUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']