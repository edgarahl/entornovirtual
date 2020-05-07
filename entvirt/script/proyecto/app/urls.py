from django.urls import path
from .views import hola_mundo, CategoriaListar, CategoriaNueva

urlpatterns = [
    path("hola-mundo", hola_mundo, name="home1"),
    path("categorias/", CategoriaListar.as_view(), name="categoria_listar"),
    path("categorias/nueva/", CategoriaNueva.as_view(), name="categoria_nueva"),
]
