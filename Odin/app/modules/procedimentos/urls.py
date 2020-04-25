from django.urls import path
from .views import ProcedimentoListView, ProcedimentoCreateView
from .views import ProcedimentoDeleteView, ProcedimentoUpdateView

urlpatterns = [

    path('', ProcedimentoListView.as_view(), name='index_procedimentos'),
    path('new', ProcedimentoCreateView.as_view(), name='new_procedimento'),
    path('update/<int:pk>/', ProcedimentoUpdateView.as_view(), name='update_procedimento'),
    path('delete/<int:pk>/', ProcedimentoDeleteView.as_view(), name='delete_procedimento')
]