# ruff: noqa
from django.urls import path
from .views import LinkListView, LinkCreateView, LinkUpdateView, LinkDeleteView

urlpatterns = [
    path('', LinkListView.as_view(), name='link-list'),
    path('create/', LinkCreateView.as_view(), name='link-create'),
    path('<int:pk>/edit/', LinkUpdateView.as_view(), name='link-edit'),
    path('<int:pk>/delete/', LinkDeleteView.as_view(), name='link-delete'),
]
