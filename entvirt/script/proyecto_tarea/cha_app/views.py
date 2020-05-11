from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Vendedor, Poliza, Asegurado, Hospital, ContratoPoliza
from django.urls import reverse_lazy
from .form import VendedorForm, PolizaForm, HospitalForm, ContratoPolizaForm, AseguradoForm


# Asi tambien se puede importar la categoria
# from .models import Categoria

# Create your views here.

def index(request):
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'cha_app/login.html'
    )

class VendedorListar(generic.ListView):
    model = Vendedor
    template_name = 'cha_app/vendedor_list.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    ordering = "nombres"


class VendedorNueva(generic.CreateView):
    model = Vendedor
    template_name = 'cha_app/vendedor_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = VendedorForm
    success_url = reverse_lazy('cha_app:vendedor_listar')


class VendedorEditar(generic.UpdateView):
    model = Vendedor
    template_name = 'cha_app/vendedor_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = VendedorForm
    success_url = reverse_lazy('cha_app:vendedor_listar')


class VendedorBorrar(generic.DeleteView):
    model = Vendedor
    template_name = 'cha_app/vendedor_borrar.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = VendedorForm
    success_url = reverse_lazy('cha_app:vendedor_borrar')


class AseguradoListar(generic.ListView):
    model = Asegurado
    template_name = 'cha_app/asegurado_list.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta


class AseguradoNuevo(generic.CreateView):
    model = Asegurado
    template_name = 'cha_app/asegurado_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = AseguradoForm
    success_url = reverse_lazy('cha_app:asegurado_listar')


class AseguradoEditar(generic.UpdateView):
    model = Asegurado
    template_name = 'cha_app/asegurado_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = AseguradoForm
    success_url = reverse_lazy('cha_app:asegurado_listar')


class AseguradoBorrar(generic.DeleteView):
    model = Asegurado
    template_name = 'cha_app/asegurado_borrar.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = AseguradoForm
    success_url = reverse_lazy('cha_app:asegurado_listar')


class PolizaListar(generic.ListView):
    model = Poliza
    template_name = 'cha_app/poliza_list.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta


class PolizaNueva(generic.CreateView):
    model = Poliza
    template_name = 'cha_app/poliza_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = PolizaForm
    success_url = reverse_lazy('cha_app:poliza_listar')


class PolizaEditar(generic.UpdateView):
    model = Poliza
    template_name = 'cha_app/poliza_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class =PolizaForm
    success_url = reverse_lazy('cha_app:poliza_listar')


class PolizaBorrar(generic.DeleteView):
    model = Poliza
    template_name = 'cha_app/poliza_borrar.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = PolizaForm
    success_url = reverse_lazy('cha_app:poliza_listar')


class HospitalListar(generic.ListView):
    model = Hospital
    template_name = 'cha_app/hospital_list.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta


class HospitalNuevo(generic.CreateView):
    model = Hospital
    template_name = 'cha_app/hospital_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = HospitalForm
    success_url = reverse_lazy('cha_app:hospital_listar')


class HospitalEditar(generic.UpdateView):
    model = Hospital
    template_name = 'cha_app/hospital_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = HospitalForm
    success_url = reverse_lazy('cha_app:hospital_listar')


class HospitalBorrar(generic.DeleteView):
    model = Hospital
    template_name = 'cha_app/hospital_borrar.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = HospitalForm
    success_url = reverse_lazy('cha_app:hospital_listar')


class ContratoPoliza(generic.CreateView):
    model = ContratoPoliza
    template_name = 'cha_app/contrato_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = ContratoPolizaForm
    success_url = reverse_lazy('cha_app:contrato_listar')