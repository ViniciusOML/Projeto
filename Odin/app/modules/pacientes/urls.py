from django.urls import path
from .views import PacienteListView, PacienteCreateView, PacienteUpdateView, PacienteDeleteView


urlpatterns = [
    # path('', views.index, name='index_pacientes'),
    path('', PacienteListView.as_view(), name='index_pacientes'),
    # path('new', views.create, name='new_paciente'),
    path('new', PacienteCreateView.as_view(), name='new_paciente'),
    # path('update/<int:id>/', views.update, name='update_paciente'),

    # Para o Django entender que está pegando o id, tem que definir o nome do campo
    # passado na url como "pk"
    path('update/<int:pk>/', PacienteUpdateView.as_view(), name='update_paciente'),


    # path('delete/<int:id>/', views.delete, name='delete_paciente')
    path('delete/<int:pk>/', PacienteDeleteView.as_view(), name='delete_paciente')
]
