from django.urls import path
from .views import ResultadoPadraoUpdateView, ResultadoPadraoDetailView

urlpatterns = [
    path('update/<int:pk>/', ResultadoPadraoUpdateView.as_view(), name='update_resultado_padrao'),
    path('show/<int:pk>/', ResultadoPadraoDetailView.as_view(), name='show_resultado_padrao'),
]