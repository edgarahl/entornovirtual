"""proyecto_tarea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from . import views
from django.urls import path, include
from .views import VendedorListar, VendedorNueva, VendedorBorrar, VendedorEditar, PolizaListar, PolizaNueva \
    , HospitalListar, HospitalNuevo, HospitalEditar, HospitalBorrar, AseguradoNuevo, AseguradoEditar, AseguradoBorrar, \
    AseguradoListar, PolizaEditar, PolizaBorrar, index, ContratoPoliza, ContratoPolizaListar

urlpatterns = [
    path("vendedores/", VendedorListar.as_view(), name="vendedor_listar"),
    path("vendedores/nuevo/", VendedorNueva.as_view(), name="vendedor_nuevo"),
    path("vendedores/editar/<int:pk>", VendedorEditar.as_view(), name="vendedor_editar"),
    path("vendedores/borrar/<int:pk>", VendedorBorrar.as_view(), name="vendedor_borrar"),
    path("polizas/", PolizaListar.as_view(), name="poliza_listar"),
    path("polizas/nuevo/", PolizaNueva.as_view(), name="poliza_nuevo"),
    path("polizas/editar/<int:pk>", PolizaEditar.as_view(), name="poliza_editar"),
    path("polizas/borrar/<int:pk>", PolizaBorrar.as_view(), name="poliza_borrar"),
    path("hospitales/", HospitalListar.as_view(), name="hospital_listar"),
    path("hospitales/nuevo/", HospitalNuevo.as_view(), name="hospital_nuevo"),
    path("hospitales/editar/<int:pk>", HospitalEditar.as_view(), name="hospital_editar"),
    path("hospitales/borrar/<int:pk>", HospitalBorrar.as_view(), name="hospital_borrar"),
    path("asegurados/nuevo/", AseguradoNuevo.as_view(), name="asegurado_nuevo"),
    path("asegurados/editar/<int:pk>", AseguradoEditar.as_view(), name="asegurado_editar"),
    path("asegurados/borrar/<int:pk>", AseguradoBorrar.as_view(), name="asegurado_borrar"),
    path("asegurados/", AseguradoListar.as_view(), name="asegurado_listar"),
    #path("login/", views.loginpage, "loginpage"),
    path("", auth_views.LoginView.as_view(template_name='cha_app/login.html'), name="login"),
    path("login/", auth_views.LoginView.as_view(template_name='cha_app/login.html'), name="login"),
    path("contratos/", ContratoPolizaListar.as_view(), name="contrato_listar"),
    path("contratos/nuevo/", ContratoPoliza.as_view(), name="contrato_nuevo"),
]
