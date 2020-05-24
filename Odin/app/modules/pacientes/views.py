# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from ...models import Paciente, Atendimento, Consulta
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


class PacienteListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'app.view_paciente'
    login_url = '/'

    model = Paciente
    template_name = 'paciente/index.html'
    context_object_name = 'pacientes'


class PacienteDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'app.view_paciente'
    login_url = '/'

    model = Paciente
    template_name = 'paciente/show.html'
    success_url = reverse_lazy('show_pacientes')

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


class PacienteCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'app.add_paciente'
    login_url = '/'

    model = Paciente
    fields = [
        'nome_completo', 'cpf', 'rg', 'data_nascimento',
        'sexo', 'tem_responsavel', 'nome_responsavel', 'rg_responsavel'
    ]
    template_name = 'paciente/novo.html'

    def get_success_url(self):
        return reverse('show_paciente', kwargs={'pk': self.object.id})


class PacienteAtendimentoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'app.add_atendimento'
    login_url = '/'

    model = Atendimento
    fields = ['lif']
    template_name = 'paciente/atendimento_novo.html'

    def form_valid(self, form):
        form.instance.paciente = Paciente.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(PacienteAtendimentoCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paciente'] = Paciente.objects.get(id=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse('show_atendimento', kwargs={'pk': self.object.id})


class PacienteUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'app.change_paciente'
    login_url = '/'

    model = Paciente
    fields = ['nome_completo', 'cpf', 'rg', 'data_nascimento',
              'sexo', 'tem_responsavel', 'nome_responsavel', 'rg_responsavel']
    template_name = 'paciente/editar.html'

    def get_success_url(self):
        return reverse('show_paciente', kwargs={'pk': self.object.id})


class PacienteDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'app.delete_paciente'
    login_url = '/'

    model = Paciente
    template_name = "paciente/excluir.html"
    success_url = reverse_lazy('index_pacientes')
    context_object_name = "paciente"
