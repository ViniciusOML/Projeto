# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from ...models import Consulta, Atendimento, ResultadoBera, ResultadoPac, ResultadoAudiometria, ResultadoPadrao
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


class ConsultaListView(LoginRequiredMixin, ListView):
    login_url = '/'

    model = Consulta
    template_name = 'consulta/index.html'
    context_object_name = 'consultas'


class ConsultaCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'

    model = Consulta
    fields = ['data_consulta', 'observacao', 'procedimento']
    template_name = 'consulta/novo.html'

    def get_success_url(self):
        return reverse('update_consulta', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.atendimento = Atendimento.objects.get(id=self.request.GET['atendimento'])
        form.save()
        return super(ConsultaCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atendimento'] = Atendimento.objects.get(id=self.kwargs['pk'])
        return context


class ConsultaDetailView(LoginRequiredMixin, DetailView):
    login_url = '/'

    model = Consulta
    template_name = 'consulta/show.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.object.procedimento.tipo_laudo == 'BERA':
            context['laudos'] = ResultadoBera.objects.filter(consulta_id=self.kwargs['pk'])
        elif self.object.procedimento.tipo_laudo == 'PAC':
            context['laudos'] = ResultadoPac.objects.filter(consulta_id=self.kwargs['pk'])
        elif self.object.procedimento.tipo_laudo == 'AUDIOMETRIA':
            context['laudos'] = ResultadoAudiometria.objects.filter(consulta_id=self.kwargs['pk'])
        else:
            context['laudos'] = ResultadoPadrao.objects.filter(consulta_id=self.kwargs['pk'])
        return context


class ConsultaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'

    model = Consulta
    fields = ['data_consulta', 'observacao', 'procedimento']
    template_name = 'consulta/editar.html'

    def get_success_url(self):
        return reverse('show_consulta', kwargs={'pk': self.object.id})


class ConsultaResultadoBeraCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'

    model = ResultadoBera
    fields = [
        'cid',
        'conclusao_exame',
        'evolucao',
        'esquerdo_picos_latencia_absoluta_I',
        'esquerdo_picos_latencia_absoluta_III',
        'esquerdo_picos_latencia_absoluta_V',
        'esquerdo_picos_latencia_absoluta_interpicos',
        'esquerdo_picos_latencia_absoluta_I_III',
        'esquerdo_picos_latencia_absoluta_I_V',
        'esquerdo_picos_latencia_absoluta_I_III',
        'esquerdo_picos_latencia_absoluta_III_V',
        'esquerdo_picos_inter_latencias_I',
        'esquerdo_picos_inter_latencias_III',
        'esquerdo_picos_inter_latencias_V',
        'esquerdo_picos_inter_latencias_interpicos',
        'esquerdo_picos_inter_latencias_I_III',
        'esquerdo_picos_inter_latencias_I_V',
        'esquerdo_picos_inter_latencias_I_III',
        'esquerdo_picos_inter_latencias_III_V',

        'direito_picos_latencia_absoluta_I',
        'direito_picos_latencia_absoluta_III',
        'direito_picos_latencia_absoluta_V',
        'direito_picos_latencia_absoluta_interpicos',
        'direito_picos_latencia_absoluta_I_III',
        'direito_picos_latencia_absoluta_I_V',
        'direito_picos_latencia_absoluta_I_III',
        'direito_picos_latencia_absoluta_III_V',
        'direito_picos_inter_latencias_I',
        'direito_picos_inter_latencias_III',
        'direito_picos_inter_latencias_V',
        'direito_picos_inter_latencias_interpicos',
        'direito_picos_inter_latencias_I_III',
        'direito_picos_inter_latencias_I_V',
        'direito_picos_inter_latencias_I_III',
        'direito_picos_inter_latencias_III_V',
    ]
    template_name = 'consulta/resultado_bera_novo.html'

    def get_success_url(self):
        return reverse('show_resultado_bera', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.consulta = Consulta.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(ConsultaResultadoBeraCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = Consulta.objects.get(id=self.kwargs['pk'])
        return context


class ConsultaResultadoPacCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'

    model = ResultadoPac
    fields = [
        'cid',
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
    template_name = 'consulta/resultado_pac_novo.html'

    def get_success_url(self):
        return reverse('show_resultado_pac', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.consulta = Consulta.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(ConsultaResultadoPacCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = Consulta.objects.get(id=self.kwargs['pk'])
        return context


class ConsultaResultadoPadraoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'

    model = ResultadoPadrao
    fields = [
        'conclusao_exame',
        'evolucao',
        'cid'
    ]
    template_name = 'consulta/resultado_padrao_novo.html'

    def form_valid(self, form):
        form.instance.consulta = Consulta.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(ConsultaResultadoPadraoCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = Consulta.objects.get(id=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse('show_resultado_padrao', kwargs={'pk': self.object.id})


class ConsultaResultadoAudiometriaCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'

    model = ResultadoAudiometria
    fields = [
        'cid',
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
    template_name = 'consulta/resultado_audiometria_novo.html'

    def get_success_url(self):
        return reverse('show_resultado_audiometria', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.consulta = Consulta.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(ConsultaResultadoAudiometriaCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = Consulta.objects.get(id=self.kwargs['pk'])
        return context


class ConsultaDeleteView(LoginRequiredMixin, DeleteView):
    model = Consulta
    template_name = "consulta/consulta_excluir.html"
    success_url = reverse_lazy('index_consultas')
    context_object_name = "consulta"
