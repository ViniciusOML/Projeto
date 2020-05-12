from django.urls import path
from .views import ResultadoPacUpdateView

urlpatterns = [
    path('update/<int:pk>/', ResultadoPacUpdateView.as_view(), name='update_resultado_pac')
]