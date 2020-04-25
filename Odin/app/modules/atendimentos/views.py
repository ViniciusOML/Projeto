# -*- encoding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from ...models import Atendimentos, Consulta, Paciente
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class AtendimentoListView(ListView):
    template_name = 'atendimento_index.html'
    model = Atendimentos
    context_object_name = 'atendimentos'
    queryset = Atendimentos.objects.all()  # Query padrão, pode ser omitid

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AtendimentoCreateView(CreateView):
    fields = ['protocolo', 'lif', 'procedimento']
    model = Atendimentos
    template_name = 'atendimento_novo.html'

    def form_valid(self, form):
        form.instance.paciente = Paciente.objects.get(id=self.request.POST['paciente'])
        form.save()
        return super(AtendimentoCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('new_consulta', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        return context



class AtendimentoUpdateView(UpdateView):
    model = Atendimentos
    fields = ['protocolo', 'paciente', 'lif', 'procedimento']
    template_name = 'atendimento_editar.html'

    success_url = reverse_lazy('index_atendimentos')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['atendimento'] = self.object
        context['consultas'] = Consulta.objects.filter(atendimento_id=self.object.id)

        return context


class AtendimentoDeleteView(DeleteView):
    model = Atendimentos
    success_url = reverse_lazy('index_atendimentos')
    template_name = "atendimento_excluir.html"
    context_object_name = "atendimento"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)