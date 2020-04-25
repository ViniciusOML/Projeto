# -*- encoding: utf-8 -*-
from django.contrib import admin
from app.models import Paciente, Atendimentos, Lif, Procedimento, Consulta

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Atendimentos)
admin.site.register(Lif)
admin.site.register(Procedimento)
admin.site.register(Consulta)
