# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", include("app.urls")),  # add this
    path("pacientes/", include("app.modules.pacientes.urls")),
    path("lifs/", include("app.modules.lifs.urls")),
    path("atendimentos/", include("app.modules.atendimentos.urls")),
    path("procedimentos/", include("app.modules.procedimentos.urls")),
    path("consultas/", include("app.modules.consultas.urls")),
    path("beras/", include("app.modules.beras.urls")),
    path("pacs/", include("app.modules.pacs.urls")),
]
