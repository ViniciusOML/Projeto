from django.urls import path
from .views import ConsultaListView,\
    ConsultaCreateView,\
    ConsultaResultadoBeraCreateView,\
    ConsultaDeleteView,\
    ConsultaUpdateView,\
    ConsultaResultadoPacCreateView,\
    ConsultaResultadoAudiometriaCreateView,\
    ConsultaResultadoPadraoCreateView,\
    ConsultaDetailView

urlpatterns = [

    path('', ConsultaListView.as_view(), name='index_consultas'),
    path('new/<int:pk>/', ConsultaCreateView.as_view(), name='new_consulta2'),
    path('update/<int:pk>/', ConsultaUpdateView.as_view(), name='update_consulta'),
    path('show/<int:pk>/', ConsultaDetailView.as_view(), name='show_consulta'),
    path('<int:pk>/resultados_bera/new', ConsultaResultadoBeraCreateView.as_view(), name='new_consulta_resultado_bera'),
    path('<int:pk>/resultados_pac/new', ConsultaResultadoPacCreateView.as_view(), name='new_consulta_resultado_pac'),
    path('<int:pk>/resultados_audiometria/new', ConsultaResultadoAudiometriaCreateView.as_view(), name='new_consulta_resultado_audiometria'),
    path('<int:pk>/resultados_padrao/new', ConsultaResultadoPadraoCreateView.as_view(), name='new_consulta_resultado_padrao'),
]