# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from ...models import Procedimento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

fields_form = [
    'nome_procedimento',
    'sigla',
    'tipo_laudo'
]


class ProcedimentoListView(LoginRequiredMixin, ListView):
    login_url = '/'

    model = Procedimento
    template_name = 'procedimento/index.html'
    context_object_name = 'procedimentos'


class ProcedimentoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'app.add_procedimento'
    login_url = '/'

    model = Procedimento
    fields = fields_form
    template_name = 'procedimento/novo.html'
    success_url = reverse_lazy('index_procedimentos')


class ProcedimentoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'app.change_procedimento'
    login_url = '/'

    model = Procedimento
    fields = fields_form
    template_name = 'procedimento/editar.html'
    success_url = reverse_lazy('index_procedimentos')


class ProcedimentoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'app.delete_procedimento'
    login_url = ''

    model = Procedimento
    template_name = "procedimento/excluir.html"
    success_url = reverse_lazy('index_procedimentos')
    context_object_name = "procedimento"
