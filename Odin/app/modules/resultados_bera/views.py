# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from ...models import ResultadoBera
from django.views.generic import UpdateView, DetailView


class ResultadoBeraDetailView(LoginRequiredMixin, DetailView):
    login_url = '/'

    model = ResultadoBera
    template_name = 'resultado/bera_show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = self.object.consulta
        context['resultado'] = self.object

        return context


class ResultadoBeraUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'

    model = ResultadoBera
    fields = [
        'cid',
        'conclusao_exame',
        'evolucao',
        'esquerdo_picos_latencia_absoluta_I',
        'esquerdo_picos_latencia_absoluta_III',
        'esquerdo_picos_latencia_absoluta_V',
        'esquerdo_picos_latencia_absoluta_interpicos',
        'esquerdo_picos_latencia_absoluta_I_III',
        'esquerdo_picos_latencia_absoluta_I_V',
        'esquerdo_picos_latencia_absoluta_I_III',
        'esquerdo_picos_latencia_absoluta_III_V',
        'esquerdo_picos_inter_latencias_I',
        'esquerdo_picos_inter_latencias_III',
        'esquerdo_picos_inter_latencias_V',
        'esquerdo_picos_inter_latencias_interpicos',
        'esquerdo_picos_inter_latencias_I_III',
        'esquerdo_picos_inter_latencias_I_V',
        'esquerdo_picos_inter_latencias_I_III',
        'esquerdo_picos_inter_latencias_III_V',

        'direito_picos_latencia_absoluta_I',
        'direito_picos_latencia_absoluta_III',
        'direito_picos_latencia_absoluta_V',
        'direito_picos_latencia_absoluta_interpicos',
        'direito_picos_latencia_absoluta_I_III',
        'direito_picos_latencia_absoluta_I_V',
        'direito_picos_latencia_absoluta_I_III',
        'direito_picos_latencia_absoluta_III_V',
        'direito_picos_inter_latencias_I',
        'direito_picos_inter_latencias_III',
        'direito_picos_inter_latencias_V',
        'direito_picos_inter_latencias_interpicos',
        'direito_picos_inter_latencias_I_III',
        'direito_picos_inter_latencias_I_V',
        'direito_picos_inter_latencias_I_III',
        'direito_picos_inter_latencias_III_V',
    ]
    template_name = 'resultado/bera_editar.html'

    def get_success_url(self):
        return reverse('show_resultado_bera', args=(self.object.id,))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = self.object.consulta
        return context
