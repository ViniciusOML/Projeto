# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from ...models import ResultadoPac
from django.views.generic import UpdateView


class ResultadoPacUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'

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

    def get_success_url(self):
        return reverse('update_consulta', args=(self.object.consulta.id,))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = self.object.consulta
        return context
