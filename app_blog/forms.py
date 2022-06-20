from dataclasses import field
from pyexpat import model
from django import forms
from app_blog.models import Obra_arq, Arquitecto

class obras_arq_view_form(forms.ModelForm):
    class Meta:
        model =  Obra_arq
        fields = '__all__'

class arquitecto_view_form(forms.ModelForm):
    class Meta:
        model = Arquitecto()
        fields = '__all__'