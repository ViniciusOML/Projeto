from django.urls import path
from .views import AudiUpdateView

urlpatterns = [
    path('update/<int:pk>/', AudiUpdateView.as_view(), name='update_audi')
]