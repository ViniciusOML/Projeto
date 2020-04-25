from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from ...models import Procedimento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class ProcedimentoListView(ListView):
    template_name = 'procedimento_index.html'
    model = Procedimento
    context_object_name = 'procedimentos'
    queryset = Procedimento.objects.all()  # Query padrão, pode ser omitid

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProcedimentoCreateView(CreateView):
    success_url = reverse_lazy('index_procedimentos')
    model = Procedimento
    fields = ['nome_procedimento', 'sigla']
    template_name = 'procedimento_novo.html'


class ProcedimentoUpdateView(UpdateView):
    model = Procedimento
    fields = ['nome_procedimento', 'sigla']
    template_name = 'procedimento_editar.html'

    success_url = reverse_lazy('index_procedimentos')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProcedimentoDeleteView(DeleteView):
    model = Procedimento
    success_url = reverse_lazy('index_procedimentos')
    template_name = "procedimento_excluir.html"
    context_object_name = "procedimento"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
