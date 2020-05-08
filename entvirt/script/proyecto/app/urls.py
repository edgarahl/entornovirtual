from django.urls import path
from .views import hola_mundo, CategoriaListar, CategoriaNueva, CategoriaEditar, CategoriaBorrar, \
    SubCategoriaListar, subCategoriaNueva

urlpatterns = [
    path("hola-mundo", hola_mundo, name="home1"),
    path("categorias/", CategoriaListar.as_view(), name="categoria_listar"),
    path("categorias/nueva/", CategoriaNueva.as_view(), name="categoria_nueva"),
    path("categorias/editar/<int:pk>", CategoriaEditar.as_view(), name="categoria_editar"),
    path("categorias/borrar/<int:pk>", CategoriaBorrar.as_view(), name="categoria_borrar"),

    path("sub-categorias/", SubCategoriaListar.as_view(), name="subcategoria_listar"),
    path("sub-categorias/nueva", subCategoriaNueva.as_view(), name="subcategoria_nueva"),
]
