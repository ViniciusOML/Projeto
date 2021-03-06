from django.db import models, transaction, IntegrityError
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
    codigo_lif_atual = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('index_lifs', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nome_lif


class Procedimento(models.Model):
    tipos_laudos = (
        ['PADRAO', 'Padrão'],
        ['BERA', 'Bera'],
        ['PAC', 'Pac'],
        ['AUDIOMETRIA', 'Audiometria'],
    )

    sigla = models.CharField(max_length=50)
    nome_procedimento = models.CharField(max_length=50)
    tipo_laudo = models.CharField(max_length=20, choices=tipos_laudos, default='PADRAO')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('index_procedimentos', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nome_procedimento


class Atendimento(models.Model):
    paciente = models.ForeignKey(to=Paciente, on_delete=models.PROTECT)
    lif = models.ForeignKey(to=Lif, on_delete=models.PROTECT)
    codigo_lif = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('paciente', 'lif',)

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                with transaction.atomic():
                    lif = Lif.objects.get(id=self.lif.id)
                    lif.codigo_lif_atual += 1
                    lif.save()

                    self.codigo_lif = self.lif.codigo_lif_atual
                    super(Atendimento, self).save(*args, **kwargs)
            except Exception as e:
                transaction.rollback()
                print(e)
        else:
            super(Atendimento, self).save(*args, **kwargs)

    def __str__(self):
        return self.codigo_lif


class Consulta(models.Model):
    atendimento = models.ForeignKey(to=Atendimento, on_delete=models.PROTECT)
    procedimento = models.ForeignKey(to=Procedimento, on_delete=models.PROTECT)
    data_consulta = models.DateField()
    observacao = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Cid(models.Model):

    codigo_cid = models.CharField(max_length=15)
    nome_cid = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('index_cids', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nome_cid

class ResultadoBera(models.Model):
    consulta = models.ForeignKey(to=Consulta, on_delete=models.PROTECT)
    cid = models.ForeignKey(to=Cid, on_delete=models.PROTECT, null = True, blank = True)

    # Esquerdo
    # picos_latencia_absoluta
    esquerdo_picos_latencia_absoluta_I = \
        models.CharField(max_length=10, blank=True)
    esquerdo_picos_latencia_absoluta_III = \
        models.CharField(max_length=10, blank=True)
    esquerdo_picos_latencia_absoluta_V = \
        models.CharField(max_length=10, blank=True)

    esquerdo_picos_latencia_absoluta_interpicos = \
        models.CharField(max_length=10, blank=True)

    esquerdo_picos_latencia_absoluta_I_III = \
        models.CharField(max_length=10, blank=True)
    esquerdo_picos_latencia_absoluta_I_V = \
        models.CharField(max_length=10, blank=True)
    esquerdo_picos_latencia_absoluta_III_V = \
        models.CharField(max_length=10, blank=True)

    # picos_inter_latencias
    esquerdo_picos_inter_latencias_I = \
        models.CharField(max_length=10, blank=True)
    esquerdo_picos_inter_latencias_III = \
        models.CharField(max_length=10, blank=True)
    esquerdo_picos_inter_latencias_V = \
        models.CharField(max_length=10, blank=True)

    esquerdo_picos_inter_latencias_interpicos = \
        models.CharField(max_length=10, blank=True)

    esquerdo_picos_inter_latencias_I_III = \
        models.CharField(max_length=10, blank=True)
    esquerdo_picos_inter_latencias_I_V = \
        models.CharField(max_length=10, blank=True)
    esquerdo_picos_inter_latencias_III_V = \
        models.CharField(max_length=10, blank=True)

    # DIREITO
    # picos_latencia_absoluta
    direito_picos_latencia_absoluta_I = \
        models.CharField(max_length=10, blank=True)
    direito_picos_latencia_absoluta_III = \
        models.CharField(max_length=10, blank=True)
    direito_picos_latencia_absoluta_V = \
        models.CharField(max_length=10, blank=True)

    direito_picos_latencia_absoluta_interpicos = \
        models.CharField(max_length=10, blank=True)

    direito_picos_latencia_absoluta_I_III = \
        models.CharField(max_length=10, blank=True)
    direito_picos_latencia_absoluta_I_V = \
        models.CharField(max_length=10, blank=True)
    direito_picos_latencia_absoluta_III_V = \
        models.CharField(max_length=10, blank=True)

    # picos_inter_latencias
    direito_picos_inter_latencias_I = \
        models.CharField(max_length=10, blank=True)
    direito_picos_inter_latencias_III = \
        models.CharField(max_length=10, blank=True)
    direito_picos_inter_latencias_V = \
        models.CharField(max_length=10, blank=True)

    direito_picos_inter_latencias_interpicos = \
        models.CharField(max_length=10, blank=True)

    direito_picos_inter_latencias_I_III = \
        models.CharField(max_length=10, blank=True)
    direito_picos_inter_latencias_I_V = \
        models.CharField(max_length=10, blank=True)
    direito_picos_inter_latencias_III_V = \
        models.CharField(max_length=10, blank=True)

    evolucao = models.TextField(null=True, blank=True)
    conclusao_exame = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ResultadoPac(models.Model):
    consulta = models.ForeignKey(to=Consulta, on_delete=models.PROTECT)
    cid = models.ForeignKey(to=Cid, on_delete=models.PROTECT, null = True, blank = True)

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

    evolucao = models.TextField(null=True, blank=True)
    conclusao_exame = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ResultadoPadrao(models.Model):
    consulta = models.ForeignKey(to=Consulta, on_delete=models.PROTECT)
    cid = models.ForeignKey(to=Cid, on_delete=models.PROTECT, null = True, blank = True)
    evolucao = models.TextField(null=True, blank=True)
    conclusao_exame = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ResultadoAudiometria(models.Model):
    consulta = models.ForeignKey(to=Consulta, on_delete=models.PROTECT)
    cid = models.ForeignKey(to=Cid, on_delete=models.PROTECT, null = True, blank = True)

    esquerdo_frequencia_250_limiar_va = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_500_limiar_va = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_1000_limiar_va = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_1500_limiar_va = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_2000_limiar_va = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_3000_limiar_va = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_4000_limiar_va = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_6000_limiar_va = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_8000_limiar_va = \
        models.CharField(max_length=10, blank=True)

    esquerdo_frequencia_250_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_500_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_1000_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_1500_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_2000_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_3000_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_4000_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_6000_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_8000_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)

    esquerdo_frequencia_250_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_500_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_1000_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_1500_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_2000_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_3000_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_4000_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_6000_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_8000_limiar_vo = \
        models.CharField(max_length=10, blank=True)

    esquerdo_frequencia_250_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_500_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_1000_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_1500_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_2000_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_3000_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_4000_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_6000_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    esquerdo_frequencia_8000_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)

    direito_frequencia_250_limiar_va = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_500_limiar_va = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_1000_limiar_va = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_1500_limiar_va = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_2000_limiar_va = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_3000_limiar_va = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_4000_limiar_va = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_6000_limiar_va = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_8000_limiar_va = \
        models.CharField(max_length=10, blank=True)

    direito_frequencia_250_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_500_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_1000_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_1500_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_2000_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_3000_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_4000_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_6000_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_8000_limiar_va_mascaramento = \
        models.CharField(max_length=10, blank=True)

    direito_frequencia_250_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_500_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_1000_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_1500_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_2000_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_3000_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_4000_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_6000_limiar_vo = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_8000_limiar_vo = \
        models.CharField(max_length=10, blank=True)

    direito_frequencia_250_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_500_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_1000_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_1500_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_2000_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_3000_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_4000_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_6000_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)
    direito_frequencia_8000_limiar_vo_mascaramento = \
        models.CharField(max_length=10, blank=True)

    esquerdo_srt = models.CharField(max_length=10, blank=True)
    esquerdo_irf_dB = models.CharField(max_length=10, blank=True)
    esquerdo_irf_porcentagem = models.CharField(max_length=10, blank=True)

    direito_srt = models.CharField(max_length=10, blank=True)
    direito_irf_dB = models.CharField(max_length=10, blank=True)
    direito_irf_porcentagem = models.CharField(max_length=10, blank=True)

    esquerdo_pressao = models.CharField(max_length=10, blank=True)
    esquerdo_maximo_relax = models.CharField(max_length=10, blank=True)
    esquerdo_compilancia_200 = models.CharField(max_length=10, blank=True)
    esquerdo_compilancia_estatica = models.CharField(max_length=10, blank=True)

    direito_pressao = models.CharField(max_length=10, blank=True)
    direito_maximo_relax = models.CharField(max_length=10, blank=True)
    direito_compilancia_200 = models.CharField(max_length=10, blank=True)
    direito_compilancia_estatica = models.CharField(max_length=10, blank=True)

    esquerdo_timpanometria = models.CharField(max_length=10, blank=True)
    direito_timpanometria = models.CharField(max_length=10, blank=True)

    esquerdo_reflexo_frequencia_500_limiar = \
        models.CharField(max_length=10, blank=True)
    esquerdo_reflexo_frequencia_1000_limiar = \
        models.CharField(max_length=10, blank=True)
    esquerdo_reflexo_frequencia_2000_limiar = \
        models.CharField(max_length=10, blank=True)
    esquerdo_reflexo_frequencia_4000_limiar = \
        models.CharField(max_length=10, blank=True)

    esquerdo_reflexo_frequencia_500_contra = \
        models.CharField(max_length=10, blank=True)
    esquerdo_reflexo_frequencia_1000_contra = \
        models.CharField(max_length=10, blank=True)
    esquerdo_reflexo_frequencia_2000_contra = \
        models.CharField(max_length=10, blank=True)
    esquerdo_reflexo_frequencia_4000_contra = \
        models.CharField(max_length=10, blank=True)

    esquerdo_reflexo_frequencia_500_diferenca = \
        models.CharField(max_length=10, blank=True)
    esquerdo_reflexo_frequencia_1000_diferenca = \
        models.CharField(max_length=10, blank=True)
    esquerdo_reflexo_frequencia_2000_diferenca = \
        models.CharField(max_length=10, blank=True)
    esquerdo_reflexo_frequencia_4000_diferenca = \
        models.CharField(max_length=10, blank=True)

    esquerdo_reflexo_frequencia_500_ipsi = \
        models.CharField(max_length=10, blank=True)
    esquerdo_reflexo_frequencia_1000_ipsi = \
        models.CharField(max_length=10, blank=True)
    esquerdo_reflexo_frequencia_2000_ipsi = \
        models.CharField(max_length=10, blank=True)
    esquerdo_reflexo_frequencia_4000_ipsi = \
        models.CharField(max_length=10, blank=True)

    direito_reflexo_frequencia_500_limiar = \
        models.CharField(max_length=10, blank=True)
    direito_reflexo_frequencia_1000_limiar = \
        models.CharField(max_length=10, blank=True)
    direito_reflexo_frequencia_2000_limiar = \
        models.CharField(max_length=10, blank=True)
    direito_reflexo_frequencia_4000_limiar = \
        models.CharField(max_length=10, blank=True)

    direito_reflexo_frequencia_500_contra = \
        models.CharField(max_length=10, blank=True)
    direito_reflexo_frequencia_1000_contra = \
        models.CharField(max_length=10, blank=True)
    direito_reflexo_frequencia_2000_contra = \
        models.CharField(max_length=10, blank=True)
    direito_reflexo_frequencia_4000_contra = \
        models.CharField(max_length=10, blank=True)

    direito_reflexo_frequencia_500_diferenca = \
        models.CharField(max_length=10, blank=True)
    direito_reflexo_frequencia_1000_diferenca = \
        models.CharField(max_length=10, blank=True)
    direito_reflexo_frequencia_2000_diferenca = \
        models.CharField(max_length=10, blank=True)
    direito_reflexo_frequencia_4000_diferenca = \
        models.CharField(max_length=10, blank=True)

    direito_reflexo_frequencia_500_ipsi = \
        models.CharField(max_length=10, blank=True)
    direito_reflexo_frequencia_1000_ipsi = \
        models.CharField(max_length=10, blank=True)
    direito_reflexo_frequencia_2000_ipsi = \
        models.CharField(max_length=10, blank=True)
    direito_reflexo_frequencia_4000_ipsi = \
        models.CharField(max_length=10, blank=True)

    evolucao = models.TextField(null=True, blank=True)
    conclusao_exame = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
