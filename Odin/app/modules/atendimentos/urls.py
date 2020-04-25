from django.urls import path
from .views import AtendimentoListView, AtendimentoUpdateView
from .views import AtendimentoDeleteView, AtendimentoCreateView

urlpatterns = [
    path('', AtendimentoListView.as_view(), name='index_atendimentos'),
    path('new', AtendimentoCreateView.as_view(), name='new_atendimento'),
    path('update/<int:pk>/', AtendimentoUpdateView.as_view(), name='update_atendimento'),
    path('delete/<int:pk>/', AtendimentoDeleteView.as_view(), name='delete_atendimento')
]
