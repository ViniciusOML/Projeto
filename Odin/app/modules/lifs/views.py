# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from ...models import Lif
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class LifListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'app.view_lif'
    login_url = '/'

    model = Lif
    template_name = 'lif/index.html'
    context_object_name = 'lifs'


class LifCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'app.add_lif'
    login_url = '/'

    model = Lif
    fields = ['nome_lif']
    template_name = 'lif/novo.html'
    success_url = reverse_lazy('index_lifs')


class LifUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'app.change_lif'
    login_url = '/'

    model = Lif
    fields = ['nome_lif', 'codigo_lif_atual']
    template_name = 'lif/editar.html'
    success_url = reverse_lazy('index_lifs')


class LifDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'app.delete_lif'
    login_url = '/'

    model = Lif
    template_name = "lif/excluir.html"
    success_url = reverse_lazy('index_lifs')
    context_object_name = "lif"
