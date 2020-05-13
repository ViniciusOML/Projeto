# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from ...models import ResultadoPac
from django.views.generic import UpdateView, DetailView


class ResultadoPacDetailView(LoginRequiredMixin, DetailView):
    login_url = '/'

    model = ResultadoPac
    template_name = 'resultado/pac_show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = self.object.consulta
        context['resultado'] = self.object

        return context


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
    template_name = 'resultado/pac_editar.html'

    def get_success_url(self):
        return reverse('show_resultado_pac', args=(self.object.id,))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = self.object.consulta
        return context
