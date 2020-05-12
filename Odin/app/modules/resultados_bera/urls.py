from django.urls import path
from .views import ResultadoBeraUpdateView

urlpatterns = [
    path('update/<int:pk>/', ResultadoBeraUpdateView.as_view(), name='update_resultado_bera')
]