from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from ...models import ResultadoBera
from django.views.generic import UpdateView


class ResultadoBeraUpdateView(UpdateView):
    model = ResultadoBera
    fields = [
        'conclusao_exame',
        'evolucao',
        'esquerdo_picos_latencia_abosoluta_I',
        'esquerdo_picos_latencia_abosoluta_III',
        'esquerdo_picos_latencia_abosoluta_V',
        'esquerdo_picos_latencia_abosoluta_interpicos',
        'esquerdo_picos_latencia_abosoluta_I_III',
        'esquerdo_picos_latencia_abosoluta_I_V',
        'esquerdo_picos_latencia_abosoluta_I_III',
        'esquerdo_picos_latencia_abosoluta_III_V',
        'esquerdo_picos_inter_latencias_I',
        'esquerdo_picos_inter_latencias_III',
        'esquerdo_picos_inter_latencias_V',
        'esquerdo_picos_inter_latencias_interpicos',
        'esquerdo_picos_inter_latencias_I_III',
        'esquerdo_picos_inter_latencias_I_V',
        'esquerdo_picos_inter_latencias_I_III',
        'esquerdo_picos_inter_latencias_III_V',

        'direito_picos_latencia_abosoluta_I',
        'direito_picos_latencia_abosoluta_III',
        'direito_picos_latencia_abosoluta_V',
        'direito_picos_latencia_abosoluta_interpicos',
        'direito_picos_latencia_abosoluta_I_III',
        'direito_picos_latencia_abosoluta_I_V',
        'direito_picos_latencia_abosoluta_I_III',
        'direito_picos_latencia_abosoluta_III_V',
        'direito_picos_inter_latencias_I',
        'direito_picos_inter_latencias_III',
        'direito_picos_inter_latencias_V',
        'direito_picos_inter_latencias_interpicos',
        'direito_picos_inter_latencias_I_III',
        'direito_picos_inter_latencias_I_V',
        'direito_picos_inter_latencias_I_III',
        'direito_picos_inter_latencias_III_V',
    ]
    template_name = 'bera_editar.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('update_consulta', args=(self.object.consulta.id,))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = self.object.consulta
        return context
