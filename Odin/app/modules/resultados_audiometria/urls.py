from django.urls import path
from .views import ResultadoAudiometriaUpdateView

urlpatterns = [
    path('update/<int:pk>/', ResultadoAudiometriaUpdateView.as_view(), name='update_audi')
]