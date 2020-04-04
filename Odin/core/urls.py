# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("authentication.urls")),  # add this
    path("", include("app.urls")),  # add this
    path("pacientes/", include("app.modules.pacientes.urls")),
    path("lifs/", include("app.modules.lifs.urls"))
]
