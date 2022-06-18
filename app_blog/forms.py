from django import forms

class obras_arq_view_form(forms.Form):
    nombre_obra = forms.CharField(max_length=100)
    ubicacion_obra = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=300)
    año = forms.IntegerField()
    tipo = forms.CharField(max_length=100)

class arquitecto_view_form(forms.Form):
    nombre_apellido_arqui = forms.CharField(max_length=100)

