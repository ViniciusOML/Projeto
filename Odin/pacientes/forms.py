from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    nome_completo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome Completo",
                "class": "form-control"
            }
        )
    )

    cpf = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "CPF",
                "class": "form-control"
            }
        )
    )

    rg = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "RG",
                "class": "form-control"
            }
        )
    )

    nome_completo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome Completo",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Paciente
        fields = [
            'nome_completo',
            'cpf',
            'rg',
            'data_nascimento',
            'sexo',
            'tem_responsavel',
            'nome_responsavel',
            'rg_responsavel'
        ]

