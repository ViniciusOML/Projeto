# -*- encoding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ...models import Paciente, Atendimentos, Consulta
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class PacienteListView(ListView):
    template_name = 'paciente_index.html'
    model = Paciente
    context_object_name = 'pacientes'
    queryset = Paciente.objects.all()  # Query padrão, pode ser omitid

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PacienteCreateView(CreateView):
    success_url = reverse_lazy('index_pacientes')
    model = Paciente
    fields = ['nome_completo', 'cpf', 'rg', 'data_nascimento',
              'sexo', 'tem_responsavel', 'nome_responsavel', 'rg_responsavel']
    template_name = 'paciente_novo.html'


class PacienteAtendimentoCreateView(CreateView):
    success_url = reverse_lazy('index_atendimentos')
    fields = ['codigo_lif', 'lif']
    model = Atendimentos
    template_name = 'paciente_atendimento_novo.html'

    def form_valid(self, form):
        form.instance.paciente = Paciente.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(PacienteAtendimentoCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paciente'] = Paciente.objects.get(id=self.kwargs['pk'])
        return context

    # def get_form(self, *args, **kwargs):
    #     form = super(CreateView, self).get_form(*args, **kwargs)        
    #     form.fields['lif'].queryset = lif_usados
    #     return form


class PacienteUpdateView(UpdateView):
    model = Paciente
    fields = ['nome_completo', 'cpf', 'rg', 'data_nascimento',
              'sexo', 'tem_responsavel', 'nome_responsavel', 'rg_responsavel']
    template_name = 'paciente_editar.html'

    success_url = reverse_lazy('index_pacientes')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        atendimentos = Atendimentos.objects.filter(paciente_id=self.object.id)

        context['atendimentos'] = []
        context['consultas'] = []

        for atendimento in atendimentos:
            context['atendimentos'].append(atendimento)            

            consultas = Consulta.objects.filter(atendimento_id=atendimento.id)

            for consulta in consultas:
                context['consultas'].append(consulta)

        return context


class PacienteDeleteView(DeleteView):

    model = Paciente
    success_url = reverse_lazy('index_pacientes')
    template_name = "paciente_excluir.html"
    context_object_name = "paciente"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
