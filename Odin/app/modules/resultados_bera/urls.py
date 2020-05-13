from django.urls import path
from .views import ResultadoBeraUpdateView, ResultadoBeraDetailView

urlpatterns = [
    path('update/<int:pk>/', ResultadoBeraUpdateView.as_view(), name='update_resultado_bera'),
    path('show/<int:pk>/', ResultadoBeraDetailView.as_view(), name='show_resultado_bera'),
]