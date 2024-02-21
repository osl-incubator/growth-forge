# ruff: noqa
from django.urls import path
from .views import LinkListView, LinkCreateView, LinkUpdateView, LinkDeleteView

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('create/', LinkCreateView.as_view(), name='link-create'),
    path('edit/<int:pk>/', LinkUpdateView.as_view(), name='link-edit'),
    path('delete/<int:pk>/', LinkDeleteView.as_view(), name='link-delete'),
]
