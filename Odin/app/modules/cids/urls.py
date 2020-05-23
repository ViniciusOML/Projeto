from django.urls import path
from .views import CidListView, CidCreateView, CidDeleteView, CidUpdateView

urlpatterns = [

    path('', CidListView.as_view(), name='index_cids'),
    path('new', CidCreateView.as_view(), name='new_cid'),
    path('update/<int:pk>/', CidUpdateView.as_view(), name='update_cid'),
    path('delete/<int:pk>/', CidDeleteView.as_view(), name='delete_cid')
]
