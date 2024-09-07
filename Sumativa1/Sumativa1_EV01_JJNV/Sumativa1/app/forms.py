from django import forms
from .models import Trabajador, Cargo, Departamento

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese los apellidos'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el RUT'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la dirección'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'licencia_conducir': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Ingrese observaciones (al menos 5 palabras)'}),
        }

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        return rut

    def clean_observaciones(self):
        observaciones = self.cleaned_data.get('observaciones')
        palabras = observaciones.split()
        if len(palabras) < 5:
            raise forms.ValidationError("Las observaciones deben contener al menos 5 palabras.")
        return observaciones
