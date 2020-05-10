# -*- encoding: utf-8 -*-
from django.contrib import admin
from app.models import Paciente,\
    Atendimento,\
    Lif,\
    Procedimento,\
    Consulta,\
    ResultadoPac,\
    ResultadoBera,\
    ResultadoAudiometria

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Atendimento)
admin.site.register(Lif)
admin.site.register(Procedimento)
admin.site.register(Consulta)
admin.site.register(ResultadoPac)
admin.site.register(ResultadoBera)
admin.site.register(ResultadoAudiometria)
