from django.http import HttpResponse
from django.shortcuts import render
from app_blog.models import Obra_arq, Arquitecto
from app_blog.forms import obras_arq_view_form, arquitecto_view_form
from django.http import HttpResponse

# Create your views here.
def obras_arq_view(request):
    obras= Obra_arq.objects.all()
    context = {'obras':obras}
    return render(request,'obras_arq.html',context=context)

def detail_obrasarq(request, pk):
    try:
        obra = Obra_arq.objects.get(pk=pk)
        context = {'obras':obra}
        return render(request,'obras_arq_detail.html',context=context)
    except:
        context = {'error':'La obra no existe'}
        return render(request,'obras_arq.html',context=context)

def arquitectos_view(request):
    arquitectos= Arquitecto.objects.all()
    context = {'arquitectos':arquitectos}
    return render(request,'arquitectos.html',context=context)

def detail_arquitecto(request, pk):
    try:
        inst = Arquitecto.objects.get(pk=pk)
        context = {'inst':inst}
        return render(request,'arquitecto_detail.html',context=context)
    except:
        context = {'error':'El arquitecto no existe'}
        return render(request,'arquitectos.html',context=context)

def cargar_obra(request):
    if request.method == 'GET':
        form = obras_arq_view_form()
        context = {'form':form}
        return render(request,'cargar_obra.html',context=context)
    else:
        form = obras_arq_view_form(request.POST)
        if form.is_valid():
            new_obra = Obra_arq.objects.create(
                nombre_obra = form.cleaned_data['nombre_obra'],
                ubicacion_obra = form.cleaned_data['ubicacion_obra'],
                año = form.cleaned_data['año'],
                descripcion = form.cleaned_data['descripcion'],
                tipo = form.cleaned_data['tipo'],
            )
            context = {'new_obra':new_obra}
        else:
            context = {'errors':form.errors}
        return render(request,'cargar_obra.html',context=context)

def cargar_arqui(request):
    if request.method == 'GET':
        form = arquitecto_view_form()
        context = {'form':form}
        return render(request,'cargar_arquitecto.html',context=context)
    else:
        form = arquitecto_view_form(request.POST)
        if form.is_valid():
            new_arqui = Arquitecto.objects.create(
                nombre_arqui = form.cleaned_data['nombre_arqui'],
                apellido_arqui = form.cleaned_data['apellido_arqui'],
            )
            context = {'new_arqui':new_arqui}
        else:
            context = {'errors':form.errors}
        return render(request,'cargar_arquitecto.html',context=context)

def search_obra(request):
    obras = Obra_arq.objects.filter(nombre_obra__icontains = request.GET['search'])
    context = {'obras':obras}
    return render(request,'search_obra.html', context=context)
