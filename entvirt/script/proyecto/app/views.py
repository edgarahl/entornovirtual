from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from app.models import Categoria, SubCategoria
from django.urls import reverse_lazy
from .form import CategoriaForm, SubCategoriaForm


#Asi tambien se puede importar la categoria
#from .models import Categoria

# Create your views here.
def hola_mundo(request):
    return HttpResponse("Hola Mundo")

#vista basadas en funcions y vistas basadas en clase

class  CategoriaListar(generic.ListView):
    model=Categoria
    template_name='app/categoria_list.html'
    context_object_name='obj' # es el nombre del objeto de la consulta
    ordering="descripcion"

class CategoriaNueva(generic.CreateView):
    model=Categoria
    template_name='app/categoria_form.html'
    context_object_name='obj' # es el nombre del objeto de la consulta
    form_class=CategoriaForm
    success_url=reverse_lazy('app:categoria_listar')

class CategoriaEditar(generic.UpdateView):
    model=Categoria
    template_name='app/categoria_form.html'
    context_object_name='obj' # es el nombre del objeto de la consulta
    form_class=CategoriaForm
    success_url=reverse_lazy('app:categoria_listar')

class CategoriaBorrar(generic.DeleteView):
    model=Categoria
    template_name='app/borrar.html'
    context_object_name='obj' # es el nombre del objeto de la consulta
    form_class=CategoriaForm
    success_url=reverse_lazy('app:categoria_borrar')    

class  SubCategoriaListar(generic.ListView):
    model=SubCategoria
    template_name='app/subcategoria_list.html'
    context_object_name='obj' # es el nombre del objeto de la consulta

class subCategoriaNueva(generic.CreateView):
    model=SubCategoria
    template_name='app/subcategoria_form.html'
    context_object_name='obj' # es el nombre del objeto de la consulta
    form_class=SubCategoriaForm
    success_url=reverse_lazy('app:subcategoria_listar')
