from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from growth_forge.users.models import User

from .forms import ProjectForm
from .models import Project


class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'list.html'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'form.html'
    success_url = reverse_lazy('project-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['title'] = 'Create Project'
        return context


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'form.html'
    success_url = reverse_lazy(
        'project-list'
    )  # Adjust the URL name as necessary

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Project'
        context['button_label'] = 'Update'
        context['users'] = User.objects.all()
        return context


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'delete.html'
    success_url = reverse_lazy('project-list')
