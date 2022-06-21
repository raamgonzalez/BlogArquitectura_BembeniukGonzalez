from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 =  forms.CharField(label='Contraseña', widget = forms.PasswordInput)
    password2 =  forms.CharField(label='Repita su contraseña', widget = forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    descripcion	= forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'descripcion']
        help_texts = {k:'' for k in fields}
