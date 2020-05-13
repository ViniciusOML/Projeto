from django.urls import path
from .views import ResultadoAudiometriaUpdateView, ResultadoAudiometriaDetailView

urlpatterns = [
    path('update/<int:pk>/', ResultadoAudiometriaUpdateView.as_view(), name='update_resultado_audiometria'),
    path('show/<int:pk>/', ResultadoAudiometriaDetailView.as_view(), name='show_resultado_audiometria')
]