from django.shortcuts import render
from django.http import HttpResponse
# from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Categoria
from django.urls import reverse_lazy
from .form import CategoriaForm


# Asi tambien se puede importar la categoria
# from .models import Categoria

# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola Mundo")


# vista basadas en funcions y vistas basadas en clase

class CategoriaListar(ListView):
    model = Categoria
    template_name = 'app/categoria_list.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta


class CategoriaNueva(CreateView):
    model = Categoria
    fields = ['descripcion']
    template_name = 'app/categoria_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    #form_class = "CategoriaForm"
    success_url = reverse_lazy('app:categoria_listar')
