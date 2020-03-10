# -*- encoding: utf-8 -*-
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente
from .forms import PacienteForm
from django.views.generic import ListView, CreateView

# Create your views here.
# @login_required(login_url="/login/")
# def index(request):
#     pacientes = Paciente.objects.all()
#     return render(request, "index_pacientes.html", {'pacientes': pacientes})


@login_required(login_url="/login/")
#def create(request):
#    form = PacienteForm(request.POST or None)

#    if form.is_valid():
        #form.save()
        #return redirect("http://localhost:8000/pacientes/")
    #else:
        #errors = form.errors
        #return render(request, "novo_paciente.html", {'form': form, 'errors': errors})


@login_required(login_url="/login/")
def update(request, id):
    paciente = Paciente.objects.get(id=id)
    form = PacienteForm(request.POST or None, instance=paciente)

    if form.is_valid():
        form.save()
        return redirect("index_pacientes")
    return render(request, "editar_paciente.html", {'form': form})


@login_required(login_url="/login/")
def delete(request, id):
    paciente = Paciente.objects.get(id=id)
    paciente.delete()

    return redirect("index_pacientes")


class PacienteCreateView(CreateView):

    
    model = Paciente
    fields = ['nome_completo', 'cpf', 'rg', 'data_nascimento', 'sexo', 'tem_responsavel','nome_responsavel', 'rg_responsavel']
    template_name = 'novo_paciente.html'
    
    

class PacienteListView(ListView):

    template_name = 'index_pacientes.html'
    model = Paciente
    context_object_name = 'pacientes'
    queryset = Paciente.objects.all()  # Query padrão, pode ser omitida

    # Pode-se alterar a query, como demostra a linha abaixo
    # queryset = Paciente.objects.filter(nome_completo="bruna")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
