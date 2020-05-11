from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from ...models import Consulta, Atendimento, ResultadoBera, ResultadoPac, ResultadoAudiometria
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class ConsultaListView(ListView):
    template_name = 'consulta/index.html'
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
    template_name = 'consulta/novo.html'

    def form_valid(self, form):
        form.instance.atendimento = Atendimento.objects.get(id=self.request.GET['atendimento'])
        form.save()
        return super(ConsultaCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atendimento'] = Atendimento.objects.get(id=self.kwargs['pk'])
        return context


class ConsultaUpdateView(UpdateView):
    success_url = reverse_lazy('index_consultas')
    model = Consulta
    fields = ['data_consulta', 'data_consulta', 'observacao']
    template_name = 'consulta/editar.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atendimento'] = self.object.atendimento
        context['procedimento'] = self.object.procedimento

        if self.object.procedimento.sigla == 'BERA':
            context['laudos'] = ResultadoBera.objects.filter(consulta_id=self.kwargs['pk'])
        elif self.object.procedimento.sigla == 'PAC':
            context['laudos'] = ResultadoPac.objects.filter(consulta_id=self.kwargs['pk'])
        elif self.object.procedimento.sigla == 'AUDI':
            context['laudos'] = ResultadoAudiometria.objects.filter(consulta_id=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.save()
        return super(ConsultaUpdateView, self).form_valid(form)


class ConsultaBeraUpdateView(CreateView):
    success_url = reverse_lazy('index_consultas')
    model = ResultadoBera
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
    template_name = 'consulta/bera_novo.html'

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
    model = ResultadoPac
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
    template_name = 'consulta/pac_novo.html'

    def form_valid(self, form):
        form.instance.consulta = Consulta.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(ConsultaPacUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = Consulta.objects.get(id=self.kwargs['pk'])
        return context


class ConsultaAudiUpdateView(CreateView):
    success_url = reverse_lazy('index_consultas')
    model = ResultadoAudiometria
    fields = [
        'conclusao_exame',
        'evolucao',

        'esquerdo_frequencia_250_limiar_va',
        'esquerdo_frequencia_500_limiar_va',
        'esquerdo_frequencia_1000_limiar_va',
        'esquerdo_frequencia_1500_limiar_va',
        'esquerdo_frequencia_2000_limiar_va',
        'esquerdo_frequencia_3000_limiar_va',
        'esquerdo_frequencia_4000_limiar_va',
        'esquerdo_frequencia_6000_limiar_va',
        'esquerdo_frequencia_8000_limiar_va',

        'esquerdo_frequencia_250_limiar_va_mascaramento',
        'esquerdo_frequencia_500_limiar_va_mascaramento',
        'esquerdo_frequencia_1000_limiar_va_mascaramento',
        'esquerdo_frequencia_1500_limiar_va_mascaramento',
        'esquerdo_frequencia_2000_limiar_va_mascaramento',
        'esquerdo_frequencia_3000_limiar_va_mascaramento',
        'esquerdo_frequencia_4000_limiar_va_mascaramento',
        'esquerdo_frequencia_6000_limiar_va_mascaramento',
        'esquerdo_frequencia_8000_limiar_va_mascaramento',

        'esquerdo_frequencia_250_limiar_vo',
        'esquerdo_frequencia_500_limiar_vo',
        'esquerdo_frequencia_1000_limiar_vo',
        'esquerdo_frequencia_1500_limiar_vo',
        'esquerdo_frequencia_2000_limiar_vo',
        'esquerdo_frequencia_3000_limiar_vo',
        'esquerdo_frequencia_4000_limiar_vo',
        'esquerdo_frequencia_6000_limiar_vo',
        'esquerdo_frequencia_8000_limiar_vo',

        'esquerdo_frequencia_250_limiar_vo_mascaramento',
        'esquerdo_frequencia_500_limiar_vo_mascaramento',
        'esquerdo_frequencia_1000_limiar_vo_mascaramento',
        'esquerdo_frequencia_1500_limiar_vo_mascaramento',
        'esquerdo_frequencia_2000_limiar_vo_mascaramento',
        'esquerdo_frequencia_3000_limiar_vo_mascaramento',
        'esquerdo_frequencia_4000_limiar_vo_mascaramento',
        'esquerdo_frequencia_6000_limiar_vo_mascaramento',
        'esquerdo_frequencia_8000_limiar_vo_mascaramento',

        'direito_frequencia_250_limiar_va',
        'direito_frequencia_500_limiar_va',
        'direito_frequencia_1000_limiar_va',
        'direito_frequencia_1500_limiar_va',
        'direito_frequencia_2000_limiar_va',
        'direito_frequencia_3000_limiar_va',
        'direito_frequencia_4000_limiar_va',
        'direito_frequencia_6000_limiar_va',
        'direito_frequencia_8000_limiar_va',

        'direito_frequencia_250_limiar_va_mascaramento',
        'direito_frequencia_500_limiar_va_mascaramento',
        'direito_frequencia_1000_limiar_va_mascaramento',
        'direito_frequencia_1500_limiar_va_mascaramento',
        'direito_frequencia_2000_limiar_va_mascaramento',
        'direito_frequencia_3000_limiar_va_mascaramento',
        'direito_frequencia_4000_limiar_va_mascaramento',
        'direito_frequencia_6000_limiar_va_mascaramento',
        'direito_frequencia_8000_limiar_va_mascaramento',

        'direito_frequencia_250_limiar_vo',
        'direito_frequencia_500_limiar_vo',
        'direito_frequencia_1000_limiar_vo',
        'direito_frequencia_1500_limiar_vo',
        'direito_frequencia_2000_limiar_vo',
        'direito_frequencia_3000_limiar_vo',
        'direito_frequencia_4000_limiar_vo',
        'direito_frequencia_6000_limiar_vo',
        'direito_frequencia_8000_limiar_vo',

        'direito_frequencia_250_limiar_vo_mascaramento',
        'direito_frequencia_500_limiar_vo_mascaramento',
        'direito_frequencia_1000_limiar_vo_mascaramento',
        'direito_frequencia_1500_limiar_vo_mascaramento',
        'direito_frequencia_2000_limiar_vo_mascaramento',
        'direito_frequencia_3000_limiar_vo_mascaramento',
        'direito_frequencia_4000_limiar_vo_mascaramento',
        'direito_frequencia_6000_limiar_vo_mascaramento',
        'direito_frequencia_8000_limiar_vo_mascaramento',

        'esquerdo_srt',
        'esquerdo_irf_dB',
        'esquerdo_irf_porcentagem',
        'direito_srt',
        'direito_irf_dB',
        'direito_irf_porcentagem',

        'esquerdo_pressao',
        'esquerdo_maximo_relax',
        'esquerdo_compilancia_200',
        'esquerdo_compilancia_estatica',

        'direito_pressao',
        'direito_maximo_relax',
        'direito_compilancia_200',
        'direito_compilancia_estatica',

        'esquerdo_timpanometria',
        'direito_timpanometria',

        'esquerdo_reflexo_frequencia_500_limiar',
        'esquerdo_reflexo_frequencia_1000_limiar',
        'esquerdo_reflexo_frequencia_2000_limiar',
        'esquerdo_reflexo_frequencia_4000_limiar',

        'esquerdo_reflexo_frequencia_500_contra',
        'esquerdo_reflexo_frequencia_1000_contra',
        'esquerdo_reflexo_frequencia_2000_contra',
        'esquerdo_reflexo_frequencia_4000_contra',

        'esquerdo_reflexo_frequencia_500_diferenca',
        'esquerdo_reflexo_frequencia_1000_diferenca',
        'esquerdo_reflexo_frequencia_2000_diferenca',
        'esquerdo_reflexo_frequencia_4000_diferenca',

        'esquerdo_reflexo_frequencia_500_ipsi',
        'esquerdo_reflexo_frequencia_1000_ipsi',
        'esquerdo_reflexo_frequencia_2000_ipsi',
        'esquerdo_reflexo_frequencia_4000_ipsi',

        'direito_reflexo_frequencia_500_limiar',
        'direito_reflexo_frequencia_1000_limiar',
        'direito_reflexo_frequencia_2000_limiar',
        'direito_reflexo_frequencia_4000_limiar',

        'direito_reflexo_frequencia_500_contra',
        'direito_reflexo_frequencia_1000_contra',
        'direito_reflexo_frequencia_2000_contra',
        'direito_reflexo_frequencia_4000_contra',

        'direito_reflexo_frequencia_500_diferenca',
        'direito_reflexo_frequencia_1000_diferenca',
        'direito_reflexo_frequencia_2000_diferenca',
        'direito_reflexo_frequencia_4000_diferenca',

        'direito_reflexo_frequencia_500_ipsi',
        'direito_reflexo_frequencia_1000_ipsi',
        'direito_reflexo_frequencia_2000_ipsi',
        'direito_reflexo_frequencia_4000_ipsi',
    ]
    template_name = 'consulta/audi_novo.html'

    def form_valid(self, form):
        form.instance.consulta = Consulta.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(ConsultaAudiUpdateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = Consulta.objects.get(id=self.kwargs['pk'])
        return context


class ConsultaDeleteView(DeleteView):
    model = Consulta
    success_url = reverse_lazy('index_consultas')
    template_name = "consulta/consulta_excluir.html"
    context_object_name = "consulta"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
