from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Lif
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView



class LifListView(ListView):

    template_name = 'index_lifs.html'
    model = Lif
    context_object_name = 'lifs'
    queryset = Lif.objects.all()  # Query padrão, pode ser omitid

    # Pode-se alterar a query, como demostra a linha abaixo
    # queryset = Lif.objects.filter(nome_completo="bruna")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class LifCreateView(CreateView):
    success_url = reverse_lazy('index_lifs')
    model = Lif
    fields = ['nome_lif']
    template_name = 'novo_lif.html'


class LifUpdateView(UpdateView):
    model = Lif
    fields = ['nome_lif']
    template_name = 'editar_lif.html'

    success_url = reverse_lazy('index_lifs')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class LifDeleteView(DeleteView):

    model = Lif
    success_url = reverse_lazy('index_lifs')
    template_name = "excluir_lif.html"
    context_object_name = "lif"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
