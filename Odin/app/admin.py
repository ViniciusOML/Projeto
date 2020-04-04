# -*- encoding: utf-8 -*-
from django.contrib import admin
from app.models import Paciente, Atendimentos, Lif

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Atendimentos)
admin.site.register(Lif)
