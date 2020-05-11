from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from ...models import Procedimento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

fields_form = [
    'nome_procedimento',
    'sigla',
    'cid'
]

class ProcedimentoListView(ListView):
    template_name = 'procedimento/index.html'
    model = Procedimento
    context_object_name = 'procedimentos'
    queryset = Procedimento.objects.all()  # Query padrão, pode ser omitid

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProcedimentoCreateView(CreateView):
    template_name = 'procedimento/novo.html'
    success_url = reverse_lazy('index_procedimentos')
    model = Procedimento
    fields = fields_form


class ProcedimentoUpdateView(UpdateView):
    template_name = 'procedimento/editar.html'
    success_url = reverse_lazy('index_procedimentos')
    model = Procedimento
    fields = fields_form

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProcedimentoDeleteView(DeleteView):
    template_name = "procedimento/excluir.html"
    success_url = reverse_lazy('index_procedimentos')
    model = Procedimento
    context_object_name = "procedimento"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
