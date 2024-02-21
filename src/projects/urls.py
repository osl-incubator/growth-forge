# ruff: noqa
from django.urls import path
from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,
)

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('edit/<int:pk>/', ProjectUpdateView.as_view(), name='project-edit'),
    path(
        'delete/<int:pk>/', ProjectDeleteView.as_view(), name='project-delete'
    ),
]
