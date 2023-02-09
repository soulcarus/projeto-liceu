from django import forms
from .models import Estudante

class FormularioEstudante(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = ['numero_estudante','primeiro_nome','segundo_nome','email','curso','media']
        labels = {
            'numero_estudante': 'Numero do Estudante',
            'primeiro_nome': 'Primeiro Nome',
            'segundo_nome': 'Segundo Nome',
            'email': 'Email',
            'curso': 'Curso Matriculado',
            'media': 'Nota Média'
        }
        widgets = {
            'numero_estudante': forms.NumberInput(attrs={'class': 'form-control'}),
            'primeiro_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'curso': forms.TextInput(attrs={'class': 'form-control'}),
            'media': forms.NumberInput(attrs={'class': 'form-control'})
        }