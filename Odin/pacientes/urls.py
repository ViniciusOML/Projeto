from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_pacientes'),
    path('new', views.create, name='new_paciente'),
    path('update/<int:id>/', views.update, name='update_paciente'),
    path('delete/<int:id>/', views.delete, name='delete_paciente')
]
