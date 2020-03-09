# -*- encoding: utf-8 -*-

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente
from .forms import PacienteForm

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    pacientes = Paciente.objects.all()
    return render(request, "index_pacientes.html", {'pacientes': pacientes})


@login_required(login_url="/login/")
def create(request):
    form = PacienteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("index_pacientes")
    else:
        errors = form.errors
        return render(request, "novo_paciente.html", {'form': form, 'errors': errors})


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
