# -*- encoding: utf-8 -*-


from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator

ROLE_CHOICES = (
        ('User', 0),
        ('Specialist', 1),
        ('Admin', 2)
)

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
        
class SignUpForm(UserCreationForm):
    login = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))   
    role = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder" : "Role",                
                "class": "form-control"
            }
        ),
        validators=[
            MaxValueValidator(2),
            MinValueValidator(0)
        ])   

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('login', 'email', 'role')
