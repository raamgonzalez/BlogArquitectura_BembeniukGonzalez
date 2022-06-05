from django.shortcuts import render
from app_blog.models import Obra_arq, Inst_edu, Bibliografia

# Create your views here.
def obras_arq_view(request):
    obras= Obra_arq.objects.all()
    context = {'obras':obras}
    return render(request,'obras_arq.html',context=context)

def inst_edu_view(request):
    instituciones= Inst_edu.objects.all()
    context = {'instituciones':instituciones}
    return render(request,'inst_edu.html',context=context)

def bibliografia_view(request):
    libros = Bibliografia.objects.all()
    context = {'libros':libros}
    return render(request,'bibliografia.html',context=context)

