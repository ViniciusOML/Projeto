from django.urls import path
from .views import ConsultaListView, ConsultaCreateView, ConsultaDeleteView, ConsultaUpdateView

urlpatterns = [

    path('', ConsultaListView.as_view(), name='index_consultas'),
    path('new/<int:pk>/', ConsultaCreateView.as_view(), name='new_consulta'),
    # path('update/<int:pk>/', LifUpdateView.as_view(), name='update_lif'),
    # path('delete/<int:pk>/', LifDeleteView.as_view(), name='delete_lif')
]