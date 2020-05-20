from django import forms
from django.core.exceptions import ValidationError

from .models import Vendedor, Poliza, Hospital, Asegurado, ContratoPoliza, Doctor, Familiares, Hospitalizacion, \
    Tratamiento, DetalleTratamiento


class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombres', 'apellidos', 'estado']
        lables = {'nombres': 'Nombre', 'apellidos': 'Apellidos'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = ['descripcion', 'costo', 'costo_extension', 'valor_cobertura']
        lables = {'descripcion': 'Descripcion', 'costo': 'Costo', 'costo_extension': 'Costo de Extension'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


    def clean_valor_cobertura(self):
        v_cobertura = self.cleaned_data['valor_cobertura']
        costo = self.cleaned_data['costo']

        if costo > v_cobertura:
            raise ValidationError('Emily, El costo no puede ser mayor al valor de cobertura')
        return v_cobertura

    def clean_costo_extension(self):
        costo_e = self.cleaned_data['costo_extension']
        v_costo = self.cleaned_data['costo']
        if costo_e > v_costo:
            raise ValidationError('El costo de la extension debe ser menor al costo de la poliza')
        return costo_e


class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['descripcion', 'direccion', 'estado']
        lables = {'descripcion': 'Descripcion', 'direccion': 'Direccion', 'estado': 'Estado'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})


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
        fields = ['id_poliza', 'id_vendedor', 'id_asegurado', 'fecha_contrato', 'fecha_inicio', 'fecha_fin', ]
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
        fields = ['nombres', 'apellidos', 'estado']
        lables = {'nombres': 'Nombre', 'apellidos': 'Apellidos',
                  'estado': 'Estado'}

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({'class':'form-control'})



class FamiliaresForm(forms.ModelForm):
    class Meta:
        model = Familiares
        fields = ['nombres', 'apellidos','fecha_nacimiento']
        lables = {'asegurado': 'Nombres', 'Fecha_nacimiento': 'fecha_nacimiento', 'Apellidos': 'apellidos'}
        widgets = {
            'fecha_nacimiento': forms.DateInput(format=('%Y-%m-%d'),
                                                attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha',
                                                       'type': 'date'})
        }


class HospitalizacionForm(forms.ModelForm):
    class Meta:
        model = Hospitalizacion
        fields = ['contrato', 'hospital', 'doctor', 'fecha_entrada', 'fecha_salida']
        lables = {'contrato': 'Contrato', 'asegurado': 'Asegurado', 'hospital': 'Hospital', 'doctor': 'Doctor',
                  'fecha_entrada': 'Fecha Ingresa', 'fecha_salida': 'Fecha Egresa'}
        widgets = {
            'fecha_entrada': forms.DateInput(format=('%Y-%m-%d'),
                                             attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha',
                                                    'type': 'date'}),
            'fecha_salida': forms.DateInput(format=('%Y-%m-%d'),
                                            attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha',
                                                   'type': 'date'})
        }


class TratamientoForm(forms.ModelForm):
    class Meta:
        model = Tratamiento
        fields = ['descripcion', 'estado']
        lables = {'descripcion': 'Descripcion', 'estado': 'Estado'}


class DetalleTratamientoForm(forms.ModelForm):
    class Meta:
        model = DetalleTratamiento
        fields = ['tratamiento', 'descripcion', 'fecha', 'costo', 'estado']
        labels = {'tratamiento':'Tratamiento','fecha':'Fecha','costo':'Costo','estado':'Estado'}
        widgets = {
            'fecha': forms.DateInput(format=('%Y-%m-%d'),
                                             attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha',
                                                    'type': 'date'})
        }

    def clean_costo(self):
        costo = self.cleaned_data['costo']
        if costo == 0:
           raise ValidationError('El costo no puede ser 0')
        return costo

