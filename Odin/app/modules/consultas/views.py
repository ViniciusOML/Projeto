from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from ...models import Consulta, Atendimentos, Bera, Pac
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class ConsultaListView(ListView):

    template_name = 'consulta_index.html'
    model = Consulta
    context_object_name = 'consultas'
    queryset = Consulta.objects.all()  # Query padrão, pode ser omitid

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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atendimento'] = Atendimentos.objects.get(id=self.kwargs['pk'])
        return context


class ConsultaUpdateView(UpdateView):
    success_url = reverse_lazy('index_consultas')
    model = Consulta
    fields = ['data_consulta', 'data_consulta', 'observacao']
    template_name = 'consulta_editar.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atendimento'] = self.object.atendimento
        context['procedimento'] = self.object.procedimento

        if self.object.procedimento.sigla == 'BERA':
            context['laudos'] = Bera.objects.filter(consulta_id=self.kwargs['pk'])
        elif self.object.procedimento.sigla == 'PAC':
            context['laudos'] = Pac.objects.filter(consulta_id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.save()
        return super(ConsultaUpdateView, self).form_valid(form)


class ConsultaBeraUpdateView(CreateView):
    success_url = reverse_lazy('index_consultas')
    model = Bera
    fields = [
        'conclusao_exame',
        'evolucao',
        'esquerdo_picos_latencia_abosoluta_I',
        'esquerdo_picos_latencia_abosoluta_III',
        'esquerdo_picos_latencia_abosoluta_V',
        'esquerdo_picos_latencia_abosoluta_interpicos',
        'esquerdo_picos_latencia_abosoluta_I_III',
        'esquerdo_picos_latencia_abosoluta_I_V',
        'esquerdo_picos_latencia_abosoluta_I_III',
        'esquerdo_picos_latencia_abosoluta_III_V',
        'esquerdo_picos_inter_latencias_I',
        'esquerdo_picos_inter_latencias_III',
        'esquerdo_picos_inter_latencias_V',
        'esquerdo_picos_inter_latencias_interpicos',
        'esquerdo_picos_inter_latencias_I_III',
        'esquerdo_picos_inter_latencias_I_V',
        'esquerdo_picos_inter_latencias_I_III',
        'esquerdo_picos_inter_latencias_III_V',

        'direito_picos_latencia_abosoluta_I',
        'direito_picos_latencia_abosoluta_III',
        'direito_picos_latencia_abosoluta_V',
        'direito_picos_latencia_abosoluta_interpicos',
        'direito_picos_latencia_abosoluta_I_III',
        'direito_picos_latencia_abosoluta_I_V',
        'direito_picos_latencia_abosoluta_I_III',
        'direito_picos_latencia_abosoluta_III_V',
        'direito_picos_inter_latencias_I',
        'direito_picos_inter_latencias_III',
        'direito_picos_inter_latencias_V',
        'direito_picos_inter_latencias_interpicos',
        'direito_picos_inter_latencias_I_III',
        'direito_picos_inter_latencias_I_V',
        'direito_picos_inter_latencias_I_III',
        'direito_picos_inter_latencias_III_V',
    ]
    template_name = 'consulta_bera_novo.html'

    def form_valid(self, form):
        form.instance.consulta = Consulta.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(ConsultaBeraUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = Consulta.objects.get(id=self.kwargs['pk'])
        return context


class ConsultaPacUpdateView(CreateView):
    success_url = reverse_lazy('index_consultas')
    model = Pac
    fields = [
        'conclusao_exame',
        'evolucao',

        'esquerdo_picos_P300',
        'esquerdo_picos_P1',
        'esquerdo_picos_N1',
        'esquerdo_picos_P2',
        'esquerdo_picos_N2',

        'direito_picos_P300',
        'direito_picos_P1',
        'direito_picos_N1',
        'direito_picos_P2',
        'direito_picos_N2',
    ]
    template_name = 'consulta_pac_novo.html'

    def form_valid(self, form):
        form.instance.consulta = Consulta.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(ConsultaPacUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = Consulta.objects.get(id=self.kwargs['pk'])
        return context


class ConsultaDeleteView(DeleteView):
    model = Consulta
    success_url = reverse_lazy('index_consultas')
    template_name = "consulta_excluir.html"
    context_object_name = "consulta"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
