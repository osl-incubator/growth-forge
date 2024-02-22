from django.urls import include, path

from . import views

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('projects/', include('projects.urls')),
    path('links/', include('one_on_one.urls')),
    path('growth-plan/', include('growth_plan.urls')),
]
