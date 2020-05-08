from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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


class Lif(models.Model):

    nome_lif = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('index_lifs', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nome_lif


class Procedimento(models.Model):
    sigla = models.CharField(max_length=50)
    nome_procedimento = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('index_lifs', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nome_procedimento


class Atendimentos(models.Model):
    paciente = models.ForeignKey(to=Paciente, on_delete=models.CASCADE)
    lif = models.ForeignKey(to=Lif, on_delete=models.CASCADE)
    codigo_lif = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('paciente', 'lif',)

    def __str__(self):
        return self.codigo_lif


class Consulta(models.Model):
    atendimento = models.ForeignKey(to=Atendimentos, on_delete=models.CASCADE)
    procedimento = models.ForeignKey(to=Procedimento, on_delete=models.CASCADE)
    data_consulta = models.DateField()
    observacao = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Bera(models.Model):
    consulta = models.ForeignKey(to=Consulta, on_delete=models.CASCADE)

    # Esquerdo
    # picos_latencia_abosoluta
    esquerdo_picos_latencia_abosoluta_I = models.CharField(max_length=10, blank=True)
    esquerdo_picos_latencia_abosoluta_III = models.CharField(max_length=10, blank=True)
    esquerdo_picos_latencia_abosoluta_V = models.CharField(max_length=10, blank=True)

    esquerdo_picos_latencia_abosoluta_interpicos = models.CharField(max_length=10, blank=True)

    esquerdo_picos_latencia_abosoluta_I_III = models.CharField(max_length=10, blank=True)
    esquerdo_picos_latencia_abosoluta_I_V = models.CharField(max_length=10, blank=True)
    esquerdo_picos_latencia_abosoluta_I_III = models.CharField(max_length=10, blank=True)

    esquerdo_picos_latencia_abosoluta_III_V = models.CharField(max_length=10, blank=True)

    # picos_inter_latencias
    esquerdo_picos_inter_latencias_I = models.CharField(max_length=10, blank=True)
    esquerdo_picos_inter_latencias_III = models.CharField(max_length=10, blank=True)
    esquerdo_picos_inter_latencias_V = models.CharField(max_length=10, blank=True)

    esquerdo_picos_inter_latencias_interpicos = models.CharField(max_length=10, blank=True)

    esquerdo_picos_inter_latencias_I_III = models.CharField(max_length=10, blank=True)
    esquerdo_picos_inter_latencias_I_V = models.CharField(max_length=10, blank=True)
    esquerdo_picos_inter_latencias_I_III = models.CharField(max_length=10, blank=True)

    esquerdo_picos_inter_latencias_III_V = models.CharField(max_length=10, blank=True)

    # DIREITO
    # picos_latencia_abosoluta
    direito_picos_latencia_abosoluta_I = models.CharField(max_length=10, blank=True)
    direito_picos_latencia_abosoluta_III = models.CharField(max_length=10, blank=True)
    direito_picos_latencia_abosoluta_V = models.CharField(max_length=10, blank=True)

    direito_picos_latencia_abosoluta_interpicos = models.CharField(max_length=10, blank=True)

    direito_picos_latencia_abosoluta_I_III = models.CharField(max_length=10, blank=True)
    direito_picos_latencia_abosoluta_I_V = models.CharField(max_length=10, blank=True)
    direito_picos_latencia_abosoluta_I_III = models.CharField(max_length=10, blank=True)

    direito_picos_latencia_abosoluta_III_V = models.CharField(max_length=10, blank=True)

    # picos_inter_latencias
    direito_picos_inter_latencias_I = models.CharField(max_length=10, blank=True)
    direito_picos_inter_latencias_III = models.CharField(max_length=10, blank=True)
    direito_picos_inter_latencias_V = models.CharField(max_length=10, blank=True)

    direito_picos_inter_latencias_interpicos = models.CharField(max_length=10, blank=True)

    direito_picos_inter_latencias_I_III = models.CharField(max_length=10, blank=True)
    direito_picos_inter_latencias_I_V = models.CharField(max_length=10, blank=True)
    direito_picos_inter_latencias_I_III = models.CharField(max_length=10, blank=True)

    direito_picos_inter_latencias_III_V = models.CharField(max_length=10, blank=True)

    evolucao = models.TextField()
    conclusao_exame = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pac(models.Model):
    consulta = models.ForeignKey(to=Consulta, on_delete=models.CASCADE)

    esquerdo_picos_P300 = models.CharField(max_length=10)
    esquerdo_picos_P1 = models.CharField(max_length=10, blank=True)
    esquerdo_picos_N1 = models.CharField(max_length=10, blank=True)
    esquerdo_picos_P2 = models.CharField(max_length=10, blank=True)
    esquerdo_picos_N2 = models.CharField(max_length=10, blank=True)

    direito_picos_P300 = models.CharField(max_length=10)
    direito_picos_P1 = models.CharField(max_length=10, blank=True)
    direito_picos_N1 = models.CharField(max_length=10, blank=True)
    direito_picos_P2 = models.CharField(max_length=10, blank=True)
    direito_picos_N2 = models.CharField(max_length=10, blank=True)

    evolucao = models.TextField()
    conclusao_exame = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class LaudoPadrao(models.Model):
    consulta = models.ForeignKey(to=Consulta, on_delete=models.CASCADE)
    evolucao = models.TextField()
    conclusao_exame = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
