from ast import Index
from django.shortcuts import render
from django.views.generic import ListView
from index.models import Titulos

# Create your views here.
class Index_view(ListView):
    model = Titulos
    template_name = 'index.html'
