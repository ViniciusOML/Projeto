# -*- encoding: utf-8 -*-
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from ...models import Atendimento, Consulta, Paciente
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.sessions.models import Session


class AtendimentoListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'app.view_atendimento'
    login_url = '/'

    model = Atendimento
    template_name = 'atendimento/index.html'
    context_object_name = 'atendimentos'


class AtendimentoDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'app.view_atendimento'
    login_url = '/'

    model = Atendimento
    template_name = 'atendimento/show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['atendimento'] = self.object
        context['consultas'] = Consulta.objects.filter(atendimento_id=self.object.id)

        return context


class AtendimentoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'app.add_atendimento'
    login_url = '/'

    model = Atendimento
    fields = ['lif']
    template_name = 'atendimento/novo.html'

    def form_valid(self, form):
        form.instance.paciente = Paciente.objects.get(id=self.request.POST['paciente'])
        form.save()
        return super(AtendimentoCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pacientes'] = Paciente.objects.all()
        return context

    def get_success_url(self):
        return reverse('show_atendimento', kwargs={'pk': self.object.id})


class AtendimentoConsultaCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'app.add_consulta'
    login_url = '/'

    model = Consulta
    fields = ['data_consulta', 'observacao', 'procedimento']
    template_name = 'atendimento/consulta_novo.html'

    def form_valid(self, form):
        form.instance.atendimento = Atendimento.objects.get(id=self.kwargs['pk'])
        form.save()
        return super(AtendimentoConsultaCreateView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['atendimento'] = Atendimento.objects.get(id=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse('show_atendimento', kwargs={'pk': self.object.atendimento.id})


class AtendimentoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'app.change_atendimento'
    login_url = '/'

    model = Atendimento
    fields = ['codigo_lif', 'lif']
    template_name = 'atendimento/editar.html'

    def get_success_url(self):
        return reverse('show_atendimento', kwargs={'pk': self.object.id})


class AtendimentoDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'app.delete_atendimento'
    login_url = '/'

    model = Atendimento
    template_name = "atendimento/excluir.html"
    success_url = reverse_lazy('index_atendimentos')
    context_object_name = "atendimento"
