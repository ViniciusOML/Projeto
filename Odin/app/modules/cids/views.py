# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from ...models import Cid
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class CidListView(LoginRequiredMixin, ListView):
    login_url = '/'

    model = Cid
    template_name = 'cid/index.html'
    context_object_name = 'cids'


class CidCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'

    model = Cid
    fields = ['codigo_cid', 'nome_cid']
    template_name = 'cid/novo.html'
    success_url = reverse_lazy('index_cids')


class CidUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'

    model = Cid
    fields = ['codigo_cid', 'nome_cid']
    template_name = 'cid/editar.html'
    success_url = reverse_lazy('index_cids')


class CidDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/'

    model = Cid
    template_name = "cid/excluir.html"
    success_url = reverse_lazy('index_cids')
    context_object_name = "cid"
