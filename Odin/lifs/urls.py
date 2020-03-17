from django.urls import path
from . import views
from .views import LifListView, LifCreateView, LifDeleteView, LifUpdateView
urlpatterns = [

    path('', LifListView.as_view(), name='index_lifs'),
    path('new', LifCreateView.as_view(), name='new_lif'),
    path('update/<int:pk>/', LifUpdateView.as_view(), name='update_lif'),
    path('delete/<int:pk>/', LifDeleteView.as_view(), name='delete_lif')
]