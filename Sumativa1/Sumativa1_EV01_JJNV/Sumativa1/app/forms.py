from django import forms
from .models import Trabajador, Cargo, Departamento

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 4}),
        }

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        return rut

    def clean_observaciones(self):
        observaciones = self.cleaned_data.get('observaciones')
        palabras = observaciones.split()
        if len(palabras) < 5:
            raise forms .ValidationError("Las observaciones deben contener al menos 5 palabras.")
        return observaciones
