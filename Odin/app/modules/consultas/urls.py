from django.urls import path
from .views import ConsultaListView, ConsultaCreateView, ConsultaBeraUpdateView
from .views import ConsultaDeleteView, ConsultaUpdateView, ConsultaPacUpdateView
from .views import ConsultaAudiUpdateView

urlpatterns = [

    path('', ConsultaListView.as_view(), name='index_consultas'),
    path('new/<int:pk>/', ConsultaCreateView.as_view(), name='new_consulta2'),
    path('update/<int:pk>/', ConsultaUpdateView.as_view(), name='update_consulta'),
    path('<int:pk>/bera/new', ConsultaBeraUpdateView.as_view(), name='new_consulta_bera'),
    path('<int:pk>/pac/new', ConsultaPacUpdateView.as_view(), name='new_consulta_pac'),
    path('<int:pk>/audi/new', ConsultaAudiUpdateView.as_view(), name='new_consulta_audi'),
]