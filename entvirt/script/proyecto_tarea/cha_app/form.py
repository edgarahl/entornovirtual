from django import forms
from .models import Vendedor, Poliza, Hospital, Asegurado, ContratoPoliza, Doctor


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombres', 'apellidos', 'estado']
        lables = {'nombres': 'Nombre', 'apellidos': 'Apellidos'}


class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = ['descripcion', 'costo', 'costo_extension', 'valor_cobertura']
        lables = {'descripcion': 'Descripcion', 'costo': 'Costo', 'costo_extension': 'Costo de Extension'}


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['descripcion', 'direccion', 'estado']
        lables = {'descripcion': 'Descripcion', 'direccion': 'Direccion', 'estado': 'Estado'}


class AseguradoForm(forms.ModelForm):
    class Meta:
        model = Asegurado
        fields = ['nombres', 'apellidos', 'direccion', 'fecha_nacimiento', 'estado']
        lables = {'nombres': 'Nombre', 'apellidos': 'Apellidos', 'fecha_nacimiento': 'Fecha Nacimiento',
                  'estado': 'Estado'}
        widgets = {
            'fecha_nacimiento': forms.DateInput(format=('%Y-%m-%d'),
                                                attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha',
                                                       'type': 'date'}),
        }


class ContratoPolizaForm(forms.ModelForm):
    class Meta:
        model = ContratoPoliza
        fields = ['id_poliza', 'id_vendedor', 'id_asegurado', 'fecha_contrato', 'fecha_inicio', 'fecha_fin', 'estado']
        lables = {'id_poliza': 'Poliza', 'id_vendedor': 'Vendedor', 'id_asegurado': 'Asegurado',
                  'fecha_contrato': 'Fecha Contrato', \
                  'fecha_inicio': 'Fecha Inicio', 'fecha_fin': 'Fecha Fin', 'estado': 'Estado'}
        widgets = {
            'fecha_contrato': forms.DateInput(format=('%Y-%m-%d'),
                                              attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha',
                                                     'type': 'date'}),
            'fecha_inicio': forms.DateInput(format=('%Y-%m-%d'),
                                            attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha',
                                                   'type': 'date'}),
            'fecha_fin': forms.DateInput(format=('%Y-%m-%d'),
                                         attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha',
                                                'type': 'date'})
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombres', 'apellidos','estado']
        lables = {'nombres': 'Nombre', 'apellidos': 'Apellidos',
                  'estado': 'Estado'}



