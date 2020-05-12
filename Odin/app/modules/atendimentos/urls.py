from django.urls import path
from .views import AtendimentoListView,\
    AtendimentoUpdateView,\
    AtendimentoDeleteView,\
    AtendimentoCreateView,\
    AtendimentoConsultaCreateView,\
    AtendimentoDetailView

urlpatterns = [
    path('', AtendimentoListView.as_view(), name='index_atendimentos'),
    path('new', AtendimentoCreateView.as_view(), name='new_atendimento'),
    path('show/<int:pk>/', AtendimentoDetailView.as_view(), name='show_atendimento'),
    path('update/<int:pk>/', AtendimentoUpdateView.as_view(), name='update_atendimento'),
    path('delete/<int:pk>/', AtendimentoDeleteView.as_view(), name='delete_atendimento'),
    path('<int:pk>/consulta/new', AtendimentoConsultaCreateView.as_view(), name='new_atendimento_consulta')
]
