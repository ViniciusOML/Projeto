from django.urls import path
from .views import PacUpdateView

urlpatterns = [
    path('update/<int:pk>/', PacUpdateView.as_view(), name='update_pac')
]