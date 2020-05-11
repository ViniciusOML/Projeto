# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from ...models import Atendimento, Consulta, Paciente
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class AtendimentoListView(LoginRequiredMixin, ListView):
    login_url = '/'

    model = Atendimento
    template_name = 'atendimento/index.html'
    context_object_name = 'atendimentos'


class AtendimentoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'

    model = Atendimento
    fields = ['codigo_lif', 'lif']
    template_name = 'atendimento/novo.html'

    def form_valid(self, form):
        form.instance.paciente = Paciente.objects.get(id=self.request.POST['paciente'])
        form.save()
        return super(AtendimentoCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('new_atendimento_consulta', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        return context


class AtendimentoConsultaCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'

    model = Consulta
    fields = ['data_consulta', 'data_consulta', 'observacao', 'procedimento']
    template_name = 'atendimento/consulta_novo.html'
    success_url = reverse_lazy('index_atendimentos')

    def form_valid(self, form):
        form.instance.atendimento = Atendimento.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(AtendimentoConsultaCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atendimento'] = Atendimento.objects.get(id=self.kwargs['pk'])
        return context


class AtendimentoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'

    model = Atendimento
    fields = ['codigo_lif', 'lif']
    template_name = 'atendimento/editar.html'
    success_url = reverse_lazy('index_atendimentos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['atendimento'] = self.object
        context['consultas'] = Consulta.objects.filter(atendimento_id=self.object.id)

        return context


class AtendimentoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/'

    model = Atendimento
    template_name = "atendimento/excluir.html"
    success_url = reverse_lazy('index_atendimentos')
    context_object_name = "atendimento"
