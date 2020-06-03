# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", include("app.urls")),  # add this
    path("pacientes/", include("app.modules.pacientes.urls")),
    path("lifs/", include("app.modules.lifs.urls")),
    path("cids/", include("app.modules.cids.urls")),
    path("atendimentos/", include("app.modules.atendimentos.urls")),
    path("procedimentos/", include("app.modules.procedimentos.urls")),
    path("consultas/", include("app.modules.consultas.urls")),
    path("resultados_bera/", include("app.modules.resultados_bera.urls")),
    path("resultados_pac/", include("app.modules.resultados_pac.urls")),
    path("resultados_audiometria/", include("app.modules.resultados_audiometria.urls")),
    path("resultados_padrao/", include("app.modules.resultados_padrao.urls")),
    path("relatorios/", include("app.modules.relatorios.urls")),
]
