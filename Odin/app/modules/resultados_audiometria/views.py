from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from ...models import ResultadoAudiometria
from django.views.generic import UpdateView


class ResultadoAudiometriaUpdateView(UpdateView):
    model = ResultadoAudiometria
    fields = [
        'conclusao_exame',
        'evolucao',

        'esquerdo_frequencia_250_limiar_va',
        'esquerdo_frequencia_500_limiar_va',
        'esquerdo_frequencia_1000_limiar_va',
        'esquerdo_frequencia_1500_limiar_va',
        'esquerdo_frequencia_2000_limiar_va',
        'esquerdo_frequencia_3000_limiar_va',
        'esquerdo_frequencia_4000_limiar_va',
        'esquerdo_frequencia_6000_limiar_va',
        'esquerdo_frequencia_8000_limiar_va',

        'esquerdo_frequencia_250_limiar_va_mascaramento',
        'esquerdo_frequencia_500_limiar_va_mascaramento',
        'esquerdo_frequencia_1000_limiar_va_mascaramento',
        'esquerdo_frequencia_1500_limiar_va_mascaramento',
        'esquerdo_frequencia_2000_limiar_va_mascaramento',
        'esquerdo_frequencia_3000_limiar_va_mascaramento',
        'esquerdo_frequencia_4000_limiar_va_mascaramento',
        'esquerdo_frequencia_6000_limiar_va_mascaramento',
        'esquerdo_frequencia_8000_limiar_va_mascaramento',

        'esquerdo_frequencia_250_limiar_vo',
        'esquerdo_frequencia_500_limiar_vo',
        'esquerdo_frequencia_1000_limiar_vo',
        'esquerdo_frequencia_1500_limiar_vo',
        'esquerdo_frequencia_2000_limiar_vo',
        'esquerdo_frequencia_3000_limiar_vo',
        'esquerdo_frequencia_4000_limiar_vo',
        'esquerdo_frequencia_6000_limiar_vo',
        'esquerdo_frequencia_8000_limiar_vo',

        'esquerdo_frequencia_250_limiar_vo_mascaramento',
        'esquerdo_frequencia_500_limiar_vo_mascaramento',
        'esquerdo_frequencia_1000_limiar_vo_mascaramento',
        'esquerdo_frequencia_1500_limiar_vo_mascaramento',
        'esquerdo_frequencia_2000_limiar_vo_mascaramento',
        'esquerdo_frequencia_3000_limiar_vo_mascaramento',
        'esquerdo_frequencia_4000_limiar_vo_mascaramento',
        'esquerdo_frequencia_6000_limiar_vo_mascaramento',
        'esquerdo_frequencia_8000_limiar_vo_mascaramento',

        'direito_frequencia_250_limiar_va',
        'direito_frequencia_500_limiar_va',
        'direito_frequencia_1000_limiar_va',
        'direito_frequencia_1500_limiar_va',
        'direito_frequencia_2000_limiar_va',
        'direito_frequencia_3000_limiar_va',
        'direito_frequencia_4000_limiar_va',
        'direito_frequencia_6000_limiar_va',
        'direito_frequencia_8000_limiar_va',

        'direito_frequencia_250_limiar_va_mascaramento',
        'direito_frequencia_500_limiar_va_mascaramento',
        'direito_frequencia_1000_limiar_va_mascaramento',
        'direito_frequencia_1500_limiar_va_mascaramento',
        'direito_frequencia_2000_limiar_va_mascaramento',
        'direito_frequencia_3000_limiar_va_mascaramento',
        'direito_frequencia_4000_limiar_va_mascaramento',
        'direito_frequencia_6000_limiar_va_mascaramento',
        'direito_frequencia_8000_limiar_va_mascaramento',

        'direito_frequencia_250_limiar_vo',
        'direito_frequencia_500_limiar_vo',
        'direito_frequencia_1000_limiar_vo',
        'direito_frequencia_1500_limiar_vo',
        'direito_frequencia_2000_limiar_vo',
        'direito_frequencia_3000_limiar_vo',
        'direito_frequencia_4000_limiar_vo',
        'direito_frequencia_6000_limiar_vo',
        'direito_frequencia_8000_limiar_vo',

        'direito_frequencia_250_limiar_vo_mascaramento',
        'direito_frequencia_500_limiar_vo_mascaramento',
        'direito_frequencia_1000_limiar_vo_mascaramento',
        'direito_frequencia_1500_limiar_vo_mascaramento',
        'direito_frequencia_2000_limiar_vo_mascaramento',
        'direito_frequencia_3000_limiar_vo_mascaramento',
        'direito_frequencia_4000_limiar_vo_mascaramento',
        'direito_frequencia_6000_limiar_vo_mascaramento',
        'direito_frequencia_8000_limiar_vo_mascaramento',

        'esquerdo_srt',
        'esquerdo_irf_dB',
        'esquerdo_irf_porcentagem',

        'direito_srt',
        'direito_irf_dB',
        'direito_irf_porcentagem',

        'esquerdo_pressao',
        'esquerdo_maximo_relax',
        'esquerdo_compilancia_200',
        'esquerdo_compilancia_estatica',

        'direito_pressao',
        'direito_maximo_relax',
        'direito_compilancia_200',
        'direito_compilancia_estatica',

        'esquerdo_timpanometria',
        'direito_timpanometria',

        'esquerdo_reflexo_frequencia_500_limiar',
        'esquerdo_reflexo_frequencia_1000_limiar',
        'esquerdo_reflexo_frequencia_2000_limiar',
        'esquerdo_reflexo_frequencia_4000_limiar',

        'esquerdo_reflexo_frequencia_500_contra',
        'esquerdo_reflexo_frequencia_1000_contra',
        'esquerdo_reflexo_frequencia_2000_contra',
        'esquerdo_reflexo_frequencia_4000_contra',

        'esquerdo_reflexo_frequencia_500_diferenca',
        'esquerdo_reflexo_frequencia_1000_diferenca',
        'esquerdo_reflexo_frequencia_2000_diferenca',
        'esquerdo_reflexo_frequencia_4000_diferenca',

        'esquerdo_reflexo_frequencia_500_ipsi',
        'esquerdo_reflexo_frequencia_1000_ipsi',
        'esquerdo_reflexo_frequencia_2000_ipsi',
        'esquerdo_reflexo_frequencia_4000_ipsi',

        'direito_reflexo_frequencia_500_limiar',
        'direito_reflexo_frequencia_1000_limiar',
        'direito_reflexo_frequencia_2000_limiar',
        'direito_reflexo_frequencia_4000_limiar',

        'direito_reflexo_frequencia_500_contra',
        'direito_reflexo_frequencia_1000_contra',
        'direito_reflexo_frequencia_2000_contra',
        'direito_reflexo_frequencia_4000_contra',

        'direito_reflexo_frequencia_500_diferenca',
        'direito_reflexo_frequencia_1000_diferenca',
        'direito_reflexo_frequencia_2000_diferenca',
        'direito_reflexo_frequencia_4000_diferenca',

        'direito_reflexo_frequencia_500_ipsi',
        'direito_reflexo_frequencia_1000_ipsi',
        'direito_reflexo_frequencia_2000_ipsi',
        'direito_reflexo_frequencia_4000_ipsi',
    ]
    template_name = 'audi_editar.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('update_consulta', args=(self.object.consulta.id,))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = self.object.consulta
        return context
