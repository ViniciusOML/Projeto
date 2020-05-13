from django.urls import path
from .views import ResultadoPacUpdateView, ResultadoPacDetailView

urlpatterns = [
    path('update/<int:pk>/', ResultadoPacUpdateView.as_view(), name='update_resultado_pac'),
    path('show/<int:pk>/', ResultadoPacDetailView.as_view(), name='show_resultado_pac')
]