from django.urls import path
from .views import ResultadoPadraoUpdateView

urlpatterns = [
    path('update/<int:pk>/', ResultadoPadraoUpdateView.as_view(), name='update_resultado_padrao')
]