from django.urls import path
from .views import BeraUpdateView

urlpatterns = [
    path('update/<int:pk>/', BeraUpdateView.as_view(), name='update_bera')
]