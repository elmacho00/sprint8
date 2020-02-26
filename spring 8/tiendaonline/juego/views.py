
from django.shortcuts import render, redirect  
from .models import Producto
from .forms import ProduForm
from django.views.generic import  View, TemplateView, ListView, CreateView, UpdateView, DeleteView
from  django.urls import reverse_lazy
# Create your views here.



class ListaProdu(ListView):
        model = Producto
        template_name='juego/listar.html'
        context_object_name ='est'
        queryset = Producto.objects.all()


"""class CrearProducto(CreateView):
        model = Producto
        form_class = ProduForm
        template_name='juego/crearProdu.html'
        success_url = reverse_lazy('estudiante:listar')

class EditarEstu(UpdateView):
        model = Estudiante
        form_class = EstuForm
        template_name='estudiante/editarEstu.html'
        success_url = reverse_lazy('estudiante:listar')

        def get_context_data(self,**kwargs):
            context = super().get_context_data(**kwargs)
            context ['estudiante'] = Estudiante.objects.all()
            return context"""
          
          



