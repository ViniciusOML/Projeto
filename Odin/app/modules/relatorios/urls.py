from django.urls import path
from .views import relatorio_consultas_por_cid, relatorio_consultas_por_cid_pdf

urlpatterns = [

    path('consultas_por_cid', relatorio_consultas_por_cid , name='relatorio_consultas_por_cid')
]