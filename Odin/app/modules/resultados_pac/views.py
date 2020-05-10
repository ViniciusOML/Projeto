from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from ...models import ResultadoPac
from django.views.generic import UpdateView


class ResultadoPacUpdateView(UpdateView):
    model = ResultadoPac
    fields = [
        'conclusao_exame',
        'evolucao',

        'esquerdo_picos_P300',
        'esquerdo_picos_P1',
        'esquerdo_picos_N1',
        'esquerdo_picos_P2',
        'esquerdo_picos_N2',

        'direito_picos_P300',
        'direito_picos_P1',
        'direito_picos_N1',
        'direito_picos_P2',
        'direito_picos_N2',
    ]
    template_name = 'pac_editar.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_success_url(self):
        return reverse('update_consulta', args=(self.object.consulta.id,))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = self.object.consulta
        return context
