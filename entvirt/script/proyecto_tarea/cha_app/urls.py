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
from . import views
from django.urls import path, include
from .views import VendedorListar, VendedorNueva, VendedorBorrar, VendedorEditar, PolizaListar, PolizaNueva \
    , HospitalListar, HospitalNuevo, HospitalEditar, HospitalBorrar, AseguradoNuevo, AseguradoEditar, AseguradoBorrar, \
    AseguradoListar, PolizaEditar, PolizaBorrar, index, ContratoPoliza, ContratoPolizaListar, home, TemplateSinPrivilegio, \
    DoctorNuevo, DoctorBorrar, DoctorEditar, DoctorListar, FamiliaresBorrar, FamiliaresEditar, FamiliaresListar, \
    FamiliaresNuevo, HospitalizacionNuevo, HospitalizacionBorrar, HospitalizacionListar, HospitalizacionEditar, \
    TratamientoNuevo, TratamientoBorrar, TratamientoEditar, TratamientoListar, DetalleTratamientoNuevo, \
    DetalleTratamientoBorrar, DetalleTratamientoEditar, DetalleTratamientoListar, AseguradoFamiliarLista, ContratoPolizaEditar, \
    ContratoPolizaBorrar
from .reportes import reporte_vendedores, reporte_contrato

urlpatterns = [
    path('home', home, name='home'),
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

    # path("", views.loginpage, name="loginpage"),
    # path("login/", views.loginpage, name="loginpage"),
    path("", auth_views.LoginView.as_view(template_name='cha_app/login.html'), name="login"),
    path("", auth_views.LogoutView.as_view(template_name='cha_app/login.html'), name="logout"),
    path('sin_privilegios/', TemplateSinPrivilegio.as_view(), name='sin_privilegios'),
    # path("login/", auth_views.LoginView.as_view(template_name='cha_app/login.html'), name="login"),
    path("contratos/", ContratoPolizaListar.as_view(), name="contrato_listar"),
    path("contratos/nuevo/", ContratoPoliza.as_view(), name="contrato_nuevo"),
    path("contratos/editar/<int:pk>", ContratoPolizaEditar.as_view(), name="contrato_editar"),
    path("contratos/borrar/<int:pk>", ContratoPolizaBorrar.as_view(), name="contrato_borrar"),

    path("doctor/nuevo/", DoctorNuevo.as_view(), name="doctor_nuevo"),
    path("doctor/editar/<int:pk>", DoctorEditar.as_view(), name="doctor_editar"),
    path("doctor/borrar/<int:pk>", DoctorBorrar.as_view(), name="doctor_borrar"),
    path("doctor/", DoctorListar.as_view(), name="doctor_listar"),

    path("familiares/nuevo/<int:id>", FamiliaresNuevo.as_view(), name="familiares_nuevo"),
    path("familiares/editar/<int:pk>", FamiliaresEditar.as_view(), name="familiares_editar"),
    path("familiares/borrar/<int:pk>", FamiliaresBorrar.as_view(), name="familiares_borrar"),
    path("familiares/", AseguradoFamiliarLista.as_view(), name="familiares_listar"),
    path("familiares/listar/<int:id>", FamiliaresListar.as_view(), name="familiares_asegurado_listar"),

    path("reportes/vendedores/", reporte_vendedores, name='vendedores_print_all'),
    path("reportes/contratos/<int:id>", reporte_contrato, name='contrato_print'),

    path("hospitalizaciones/nuevo/", HospitalizacionNuevo.as_view(), name="hospitalizaciones_nuevo"),
    path("hospitalizaciones/editar/<int:pk>", HospitalizacionEditar.as_view(), name="hospitalizaciones_editar"),
    path("hospitalizaciones/borrar/<int:pk>", HospitalizacionBorrar.as_view(), name="hospitalizaciones_borrar"),
    path("hospitalizaciones/", HospitalizacionListar.as_view(), name="hospitalizaciones_listar"),

    path("tratamientos/nuevo/", TratamientoNuevo.as_view(), name="tratamiento_nuevo"),
    path("tratamientos/editar/<int:pk>", TratamientoEditar.as_view(), name="tratamiento_editar"),
    path("tratamientos/borrar/<int:pk>", TratamientoBorrar.as_view(), name="tratamiento_borrar"),
    path("tratamientos/", TratamientoListar.as_view(), name="tratamiento_listar"),


    path("detalletratamientos/nuevo/<int:id>", DetalleTratamientoNuevo.as_view(), name="detalletratamiento_nuevo"),
    path("detalletratamientos/editar/<int:pk>", DetalleTratamientoEditar.as_view(), name="detalletratamiento_editar"),
    path("detalletratamientos/borrar/<int:pk>", DetalleTratamientoBorrar.as_view(), name="detalletratamiento_borrar"),
    path("detalletratamientos/listar/<int:id>", DetalleTratamientoListar.as_view(), name="detalletratamiento_listar"),
]
