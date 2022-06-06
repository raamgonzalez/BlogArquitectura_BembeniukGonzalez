from django import forms

class obras_arq_view_form(forms.Form):
    nombre_obra = forms.CharField(max_length=100)
    autor_obra = forms.CharField(max_length=100)
    ubicacion_obra = forms.CharField(max_length=100)
    año = forms.IntegerField()
    tipo = forms.CharField(max_length=100)

class Inst_edu_form(forms.Form):
    nombre_inst = forms.CharField(max_length=100)
    ubicacion_inst = forms.CharField(max_length=100)

class Bibliografia_form(forms.Form):
    nombre_biblio = forms.CharField(max_length=100)
    autor_biblio = forms.CharField(max_length=100)