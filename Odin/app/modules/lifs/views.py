from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from ...models import Lif
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class LifListView(ListView):

    template_name = 'lif_index.html'
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
    template_name = 'lif_novo.html'


class LifUpdateView(UpdateView):
    model = Lif
    fields = ['nome_lif']
    template_name = 'lif_editar.html'

    success_url = reverse_lazy('index_lifs')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class LifDeleteView(DeleteView):

    model = Lif
    success_url = reverse_lazy('index_lifs')
    template_name = "lif_excluir.html"
    context_object_name = "lif"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
