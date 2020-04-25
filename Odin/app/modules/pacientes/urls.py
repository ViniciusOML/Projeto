from django.urls import path
from .views import PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView


urlpatterns = [
    path('', PacienteListView.as_view(), name='index_pacientes'),
    path('new', PacienteCreateView.as_view(), name='new_paciente'),
    path('update/<int:pk>/', PacienteUpdateView.as_view(), name='update_paciente'),
    path('delete/<int:pk>/', PacienteDeleteView.as_view(), name='delete_paciente')
]
