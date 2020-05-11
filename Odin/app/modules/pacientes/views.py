# -*- encoding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ...models import Paciente, Atendimento, Consulta
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class PacienteListView(ListView):
    template_name = 'paciente/index.html'
    model = Paciente
    context_object_name = 'pacientes'
    queryset = Paciente.objects.all()  # Query padrão, pode ser omitid

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PacienteCreateView(CreateView):
    template_name = 'paciente/novo.html'
    model = Paciente
    success_url = reverse_lazy('index_pacientes')

    fields = ['nome_completo', 'cpf', 'rg', 'data_nascimento',
              'sexo', 'tem_responsavel', 'nome_responsavel', 'rg_responsavel']


class PacienteAtendimentoCreateView(CreateView):
    template_name = 'paciente/novo.html'
    model = Atendimento
    success_url = reverse_lazy('index_atendimentos')

    fields = ['codigo_lif', 'lif']

    def form_valid(self, form):
        form.instance.paciente = Paciente.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(PacienteAtendimentoCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paciente'] = Paciente.objects.get(id=self.kwargs['pk'])
        return context


class PacienteUpdateView(UpdateView):
    template_name = 'paciente/editar.html'
    model = Paciente
    success_url = reverse_lazy('index_pacientes')

    fields = ['nome_completo', 'cpf', 'rg', 'data_nascimento',
              'sexo', 'tem_responsavel', 'nome_responsavel', 'rg_responsavel']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        atendimentos = Atendimento.objects.filter(paciente_id=self.object.id)

        context['atendimentos'] = []
        context['consultas'] = []

        for atendimento in atendimentos:
            context['atendimentos'].append(atendimento)            

            consultas = Consulta.objects.filter(atendimento_id=atendimento.id)

            for consulta in consultas:
                context['consultas'].append(consulta)

        return context


class PacienteDeleteView(DeleteView):
    template_name = "paciente/excluir.html"
    success_url = reverse_lazy('index_pacientes')
    model = Paciente

    context_object_name = "paciente"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
