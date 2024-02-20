from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('projects/', views.project_list, name='project_list'),
    path('project/create/', views.project_create, name='project_create'),
    path('link/create/', views.link_create, name='link_create'),
    path('feedback/create/', views.feedback_create, name='feedback_create'),
    # Add other paths as needed
]
