# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from ...models import ResultadoPadrao
from django.views.generic import UpdateView


class ResultadoPadraoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'

    model = ResultadoPadrao
    fields = [
        'conclusao_exame',
        'evolucao',
    ]
    template_name = 'resultado_padrao_editar.html'

    def get_success_url(self):
        return reverse('update_consulta', args=(self.object.consulta.id,))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = self.object.consulta
        return context
