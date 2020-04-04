# -*- encoding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ...models import Paciente, Atendimentos
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class PacienteListView(ListView):

    template_name = 'paciente_index.html'
    model = Paciente
    context_object_name = 'pacientes'
    queryset = Paciente.objects.all()  # Query padrão, pode ser omitid

    # Pode-se alterar a query, como demostra a linha abaixo
    # queryset = Paciente.objects.filter(nome_completo="bruna")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PacienteCreateView(CreateView):
    success_url = reverse_lazy('index_pacientes')
    model = Paciente
    fields = ['nome_completo', 'cpf', 'rg', 'data_nascimento',
              'sexo', 'tem_responsavel', 'nome_responsavel', 'rg_responsavel']
    template_name = 'paciente_novo.html'


class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = ['nome_completo', 'cpf', 'rg', 'data_nascimento',
              'sexo', 'tem_responsavel', 'nome_responsavel', 'rg_responsavel']
    template_name = 'paciente_editar.html'

    
    # como pegar o id que foi passado na url
    # atendimentos = Atendimentos.objects.filter(paciente_id=id)
    atendimentos = Atendimentos.objects.all()

    extra_context = {'atendimentos': atendimentos}

    success_url = reverse_lazy('index_pacientes')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PacienteDeleteView(DeleteView):

    model = Paciente
    success_url = reverse_lazy('index_pacientes')
    template_name = "paciente_excluir.html"
    context_object_name = "paciente"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
