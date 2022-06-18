from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from app_blog.models import Obra_arq, Arquitecto
from app_blog.forms import obras_arq_view_form, arquitecto_view_form
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView

class Obras_arq_view(ListView):
    model = Obra_arq
    template_name = 'obras_arq.html'

# # Create your views here.
# def obras_arq_view(request):
#     obras= Obra_arq.objects.all()
#     context = {'obras':obras}
#     return render(request,'obras_arq.html',context=context)

class Detail_obrasarq(DetailView):
    model = Obra_arq
    template_name = 'obras_arq_detail.html'

# def detail_obrasarq(request, pk):
#     try:
#         obra = Obra_arq.objects.get(pk=pk)
#         context = {'obras':obra}
#         return render(request,'obras_arq_detail.html',context=context)
#     except:
#         context = {'error':'La obra no existe'}
#         return render(request,'obras_arq.html',context=context)

class Arquitectos_view(ListView):
    model = Arquitecto
    template_name = 'arquitectos.html'

# def arquitectos_view(request):
#     arquitectos= Arquitecto.objects.all()
#     context = {'arquitectos':arquitectos}
#     return render(request,'arquitectos.html',context=context)

class Detail_arquitecto(DetailView):
    model = Arquitecto
    template_name = 'arquitecto_detail.html'

# def detail_arquitecto(request, pk):
#     try:
#         inst = Arquitecto.objects.get(pk=pk)
#         context = {'inst':inst}
#         return render(request,'arquitecto_detail.html',context=context)
#     except:
#         context = {'error':'El arquitecto no existe'}
#         return render(request,'arquitectos.html',context=context)

class Create_obra(CreateView):
    model = Obra_arq
    template_name = 'cargar_obra.html'
    fields = '__all__'
    success_url = '/app_blog/obras_arq_view'

# def cargar_obra(request):
#     if request.method == 'GET':
#         form = obras_arq_view_form()
#         context = {'form':form}
#         return render(request,'cargar_obra.html',context=context)
#     else:
#         form = obras_arq_view_form(request.POST)
#         if form.is_valid():
#             new_obra = Obra_arq.objects.create(
#                 nombre_obra = form.cleaned_data['nombre_obra'],
#                 ubicacion_obra = form.cleaned_data['ubicacion_obra'],
#                 año = form.cleaned_data['año'],
#                 descripcion = form.cleaned_data['descripcion'],
#                 tipo = form.cleaned_data['tipo'],
#             )
#             context = {'new_obra':new_obra}
#         else:
#             context = {'errors':form.errors}
#         return render(request,'cargar_obra.html',context=context)

class Create_arqui(CreateView):
    model = Arquitecto
    template_name = 'cargar_arquitecto.html'
    fields = '__all__'
    success_url = '/app_blog/arquitectos_view'
    
# def cargar_arqui(request):
#     if request.method == 'GET':
#         form = arquitecto_view_form()
#         context = {'form':form}
#         return render(request,'cargar_arquitecto.html',context=context)
#     else:
#         form = arquitecto_view_form(request.POST)
#         if form.is_valid():
#             new_arqui = Arquitecto.objects.create(
#                 nombre_arqui = form.cleaned_data['nombre_arqui'],
#                 apellido_arqui = form.cleaned_data['apellido_arqui'],
#             )
#             context = {'new_arqui':new_arqui}
#         else:
#             context = {'errors':form.errors}
#         return render(request,'cargar_arquitecto.html',context=context)

def search_obra(request):
    obras = Obra_arq.objects.filter(nombre_obra__icontains = request.GET['search'])
    context = {'obras':obras}
    return render(request,'search_obra.html', context=context)
