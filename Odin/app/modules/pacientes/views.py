# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin
from ...models import Paciente, Atendimento, Consulta
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class PacienteListView(LoginRequiredMixin, ListView):
    login_url = '/'

    model = Paciente
    template_name = 'paciente/index.html'
    context_object_name = 'pacientes'


class PacienteCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'

    model = Paciente
    fields = [
        'nome_completo', 'cpf', 'rg', 'data_nascimento',
        'sexo', 'tem_responsavel', 'nome_responsavel', 'rg_responsavel'
    ]
    template_name = 'paciente/novo.html'
    success_url = reverse_lazy('index_pacientes')


class PacienteAtendimentoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/'

    model = Atendimento
    fields = ['codigo_lif', 'lif']
    template_name = 'paciente/atendimento_novo.html'
    success_url = reverse_lazy('index_atendimentos')

    def form_valid(self, form):
        form.instance.paciente = Paciente.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(PacienteAtendimentoCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paciente'] = Paciente.objects.get(id=self.kwargs['pk'])
        return context


class PacienteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/'

    model = Paciente
    fields = ['nome_completo', 'cpf', 'rg', 'data_nascimento',
              'sexo', 'tem_responsavel', 'nome_responsavel', 'rg_responsavel']
    template_name = 'paciente/editar.html'
    success_url = reverse_lazy('index_pacientes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Obtendo os atendimentos do paciente
        atendimentos = Atendimento.objects.filter(paciente_id=self.object.id)

        context['atendimentos'] = []
        context['consultas'] = []

        for atendimento in atendimentos:
            context['atendimentos'].append(atendimento)            

            # Obtendo as consultas do atendimento
            consultas = Consulta.objects.filter(atendimento_id=atendimento.id)

            for consulta in consultas:
                context['consultas'].append(consulta)
        return context


class PacienteDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/'

    model = Paciente
    template_name = "paciente/excluir.html"
    success_url = reverse_lazy('index_pacientes')
    context_object_name = "paciente"
