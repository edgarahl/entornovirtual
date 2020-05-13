from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import generic
from .models import Vendedor, Poliza, Asegurado, Hospital, ContratoPoliza as Contratos
from django.urls import reverse_lazy
from .form import VendedorForm, PolizaForm, HospitalForm, ContratoPolizaForm, AseguradoForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Asi tambien se puede importar la categoria
# from .models import Categoria

# Create your views here.

class ClaseBase(LoginRequiredMixin, PermissionRequiredMixin):
    login_url = 'cha_app:login'


def home(request):
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'base/home.html'
    )


class SinPrivilegios(generic.TemplateView):
    template_name = 'base/sin_permisos.html'


def index(request):
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'cha_app/login.html'
    )


"""para el funcionamiento del Login
"""


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        post = User.objects.filter(username=username)
        if post:
            username = request.POST['username']
            request.session['username'] = username
            return redirect("profile")
        else:
            return render(request, 'cha_app/login.html', {})
    return render(request, 'cha_app/login.html', {})


class VendedorListar(ClaseBase, generic.ListView):
    model = Vendedor
    template_name = 'cha_app/vendedor_list.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    context = [Paginator]
    ordering = "nombres"
    paginate_by = 5
    permission_required = "cha_app.view_vendedor"
    # login_url = 'cha_app/login.html'


class VendedorNueva(ClaseBase, generic.CreateView):
    model = Vendedor
    template_name = 'cha_app/vendedor_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = VendedorForm
    success_url = reverse_lazy('cha_app:vendedor_listar')
    permission_required = "cha_app.add_vendedor"


class VendedorEditar(ClaseBase, generic.UpdateView):
    model = Vendedor
    template_name = 'cha_app/vendedor_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = VendedorForm
    success_url = reverse_lazy('cha_app:vendedor_listar')
    permission_required = "cha_app.change_vendedor"


class VendedorBorrar(ClaseBase, generic.DeleteView):
    model = Vendedor
    template_name = 'cha_app/vendedor_borrar.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = VendedorForm
    success_url = reverse_lazy('cha_app:vendedor_borrar')
    permission_required = "cha_app.delete_vendedor"

class AseguradoListar(ClaseBase, generic.ListView):
    model = Asegurado
    template_name = 'cha_app/asegurado_list.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    permission_required = "cha_app.view_asegurado"

class AseguradoNuevo(ClaseBase, generic.CreateView):
    model = Asegurado
    template_name = 'cha_app/asegurado_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = AseguradoForm
    success_url = reverse_lazy('cha_app:asegurado_listar')
    permission_required = "cha_app.add_asegurado"

class AseguradoEditar(ClaseBase, generic.UpdateView):
    model = Asegurado
    template_name = 'cha_app/asegurado_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = AseguradoForm
    success_url = reverse_lazy('cha_app:asegurado_listar')
    permission_required = "cha_app.change_asegurado"


class AseguradoBorrar(ClaseBase, generic.DeleteView):
    model = Asegurado
    template_name = 'cha_app/asegurado_borrar.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = AseguradoForm
    success_url = reverse_lazy('cha_app:asegurado_listar')
    permission_required = "cha_app.delete_asegurado"


class PolizaListar(ClaseBase, generic.ListView):
    model = Poliza
    template_name = 'cha_app/poliza_list.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    permission_required = "cha_app.view_poliza"

class PolizaNueva(ClaseBase, generic.CreateView):
    model = Poliza
    template_name = 'cha_app/poliza_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = PolizaForm
    success_url = reverse_lazy('cha_app:poliza_listar')
    permission_required = "cha_app.add_poliza"

class PolizaEditar(ClaseBase, generic.UpdateView):
    model = Poliza
    template_name = 'cha_app/poliza_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = PolizaForm
    success_url = reverse_lazy('cha_app:poliza_listar')
    permission_required = "cha_app.change_poliza"

class PolizaBorrar(ClaseBase, generic.DeleteView):
    model = Poliza
    template_name = 'cha_app/poliza_borrar.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = PolizaForm
    success_url = reverse_lazy('cha_app:poliza_listar')
    permission_required = "cha_app.delete_poliza"

class HospitalListar(ClaseBase, generic.ListView):
    model = Hospital
    template_name = 'cha_app/hospital_list.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    permission_required = "cha_app.view_hospital"

class HospitalNuevo(ClaseBase, generic.CreateView):
    model = Hospital
    template_name = 'cha_app/hospital_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = HospitalForm
    success_url = reverse_lazy('cha_app:hospital_listar')
    permission_required = "cha_app.add_hospital"

class HospitalEditar(ClaseBase, generic.UpdateView):
    model = Hospital
    template_name = 'cha_app/hospital_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = HospitalForm
    success_url = reverse_lazy('cha_app:hospital_listar')
    permission_required = "cha_app.change_hospital"

class HospitalBorrar(ClaseBase, generic.DeleteView):
    model = Hospital
    template_name = 'cha_app/hospital_borrar.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = HospitalForm
    success_url = reverse_lazy('cha_app:hospital_listar')
    permission_required = "cha_app.delete_hosptal"

class ContratoPoliza(ClaseBase, generic.CreateView):
    model = Contratos
    template_name = 'cha_app/contrato_form.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    form_class = ContratoPolizaForm
    success_url = reverse_lazy('cha_app:contrato_listar')
    permission_required = "cha_app.add_contratopoliza"


class ContratoPolizaListar(ClaseBase, generic.ListView):
    model = Contratos
    template_name = 'cha_app/contrato_list.html'
    context_object_name = 'obj'  # es el nombre del objeto de la consulta
    permission_required = "cha_app.view_contratopoliza"


"""para el funcionamiento del Login
"""


def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        post = User.objects.filter(username=username)
        if post:
            username = request.POST['username']
            request.session['username'] = username
            # return redirect("cha_app: home.html")
            return render(request, "base/home.html")
        else:
            return render(request, 'cha_app/login.html')
    return render(request, 'cha_app/login.html')
