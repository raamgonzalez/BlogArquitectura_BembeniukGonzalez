from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from app_blog.models import Obra_arq, Arquitecto
from app_blog.forms import obras_arq_view_form, arquitecto_view_form
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

class Obras_arq_view(ListView):
    model = Obra_arq
    template_name = 'obras_arq.html'

class Detail_obrasarq(DetailView):
    model = Obra_arq
    template_name = 'obras_arq_detail.html'

class Delete_obra(DeleteView):
    model = Obra_arq
    template_name = 'delete_obra.html'

    def get_success_url(self):
        return reverse('obras_arq_view')

class Update_obra(UpdateView):
    model =  Obra_arq
    template_name = 'update_obra.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_obrasarq', kwargs={'pk':self.object.pk})

class Arquitectos_view(ListView):
    model = Arquitecto
    template_name = 'arquitectos.html'

class Detail_arquitecto(DetailView):
    model = Arquitecto
    template_name = 'arquitecto_detail.html'

class Delete_arquitecto(DeleteView):
    model = Arquitecto
    template_name = 'delete_arqui.html'

    def get_success_url(self):
        return reverse('arquitectos_view')

class Update_arquitecto(UpdateView):
    model =  Arquitecto
    template_name = 'update_arqui.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_arquitecto', kwargs={'pk':self.object.pk})

class Create_obra(CreateView):
    model = Obra_arq
    template_name = 'cargar_obra.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_obrasarq', kwargs={'pk': self.object.pk})

class Create_arqui(CreateView):
    model = Arquitecto
    template_name = 'cargar_arquitecto.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_arquitecto', kwargs={'pk': self.object.pk})

def search_obra(request):
    obras = Obra_arq.objects.filter(nombre_obra__icontains = request.GET['search'])
    context = {'obras':obras}
    return render(request,'search_obra.html', context=context)
