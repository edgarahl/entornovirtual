from django import forms
from .models import Categoria, SubCategoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=['descripcion']
        labels={'descripcion':'Descripcion'}

class SubCategoriaForm(forms.ModelForm):
    class Meta:
        model=SubCategoria
        fields=['categoria','descripcion']
        labels={'categoria':'Categorias',
            'descripcion':'Descripcion'
            }