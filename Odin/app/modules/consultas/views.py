from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from ...models import Consulta, Atendimentos
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class ConsultaListView(ListView):

    template_name = 'consulta_index.html'
    model = Consulta
    context_object_name = 'consultas'
    queryset = Consulta.objects.all()  # Query padrão, pode ser omitid

    # Pode-se alterar a query, como demostra a linha abaixo
    # queryset = Lif.objects.filter(nome_completo="bruna")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ConsultaCreateView(CreateView):
    success_url = reverse_lazy('index_consultas')
    model = Consulta
    fields = ['data_consulta', 'data_consulta', 'observacao']
    template_name = 'consulta_novo.html'

    def form_valid(self, form):
        form.instance.atendimento = Atendimentos.objects.get(id=self.request.GET['atendimento'])
        form.save()
        return super(ConsultaCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atendimento'] = Atendimentos.objects.get(id=self.request.GET['atendimento'])
        return context


class ConsultaUpdateView(UpdateView):
    model = Consulta
    fields = ['nome_lif']
    template_name = 'lif_editar.html'

    success_url = reverse_lazy('index_consultas')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ConsultaDeleteView(DeleteView):
    model = Consulta
    success_url = reverse_lazy('index_consultas')
    template_name = "consulta_excluir.html"
    context_object_name = "consulta"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
