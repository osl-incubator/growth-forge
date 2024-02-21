from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.user_register, name='register'),
    path('projects/', include('projects.urls')),
    path('links/', include('linker.urls')),
    path('growth-plan/', include('growth_plan.urls')),
]
