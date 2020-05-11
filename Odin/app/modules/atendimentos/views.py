# -*- encoding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ...models import Atendimento, Consulta, Paciente
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class AtendimentoListView(ListView):
    template_name = 'atendimento/index.html'
    model = Atendimento
    context_object_name = 'atendimentos'
    queryset = Atendimento.objects.all()  # Query padrão, pode ser omitid

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class AtendimentoCreateView(CreateView):
    fields = ['codigo_lif', 'lif']
    model = Atendimento
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


class AtendimentoConsultaCreateView(CreateView):
    success_url = reverse_lazy('index_atendimentos')
    model = Consulta
    fields = ['data_consulta', 'data_consulta', 'observacao', 'procedimento']
    template_name = 'atendimento/consulta_novo.html'

    def form_valid(self, form):
        form.instance.atendimento = Atendimento.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(AtendimentoConsultaCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atendimento'] = Atendimento.objects.get(id=self.kwargs['pk'])
        return context


class AtendimentoUpdateView(UpdateView):
    model = Atendimento
    fields = ['codigo_lif', 'lif']
    template_name = 'atendimento/editar.html'

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
    model = Atendimento
    success_url = reverse_lazy('index_atendimentos')
    template_name = "atendimento/excluir.html"
    context_object_name = "atendimento"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
