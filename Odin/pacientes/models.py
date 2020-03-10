from django.db import models
from django.urls import reverse

# Create your models here.


class Paciente(models.Model):
    sexo_escolhas = [
        ("F", 'Feminino'),
        ("M", 'Masculino'),
        ("O", 'Outros')
    ]

    nome_completo = models.CharField(max_length=120)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=10)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1, choices=sexo_escolhas)
    tem_responsavel = models.BooleanField()
    nome_responsavel = models.CharField(max_length=120, blank=True)
    rg_responsavel = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('index_pacientes', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nome_completo
