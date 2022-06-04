from multiprocessing import context
from django.http import HttpResponse
from django.template import Template, Context

from datetime import datetime
from django.shortcuts import render

def index(request):
    return render(request,'index.html',context = {})