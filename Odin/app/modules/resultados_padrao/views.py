# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from ...models import ResultadoPadrao
from django.views.generic import UpdateView, DetailView


class ResultadoPadraoDetailView(LoginRequiredMixin, DetailView):
    login_url = '/'

    model = ResultadoPadrao
    template_name = 'resultado/padrao_show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = self.object.consulta
        context['resultado'] = self.object

        return context


class ResultadoPadraoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'

    model = ResultadoPadrao
    fields = [
        'cid',
        'conclusao_exame',
        'evolucao',
    ]
    template_name = 'resultado/padrao_editar.html'

    def get_success_url(self):
        return reverse('show_resultado_padrao', args=(self.object.id,))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = self.object.consulta
        return context
