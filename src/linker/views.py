# linker/views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import LinkForm
from .models import Link


class LinkListView(ListView):
    model = Link
    context_object_name = 'links'
    template_name = 'linker/link_list.html'


class LinkCreateView(CreateView):
    model = Link
    form_class = LinkForm
    template_name = 'linker/link_form.html'
    success_url = reverse_lazy('link-list')


class LinkUpdateView(UpdateView):
    model = Link
    form_class = LinkForm
    template_name = 'linker/link_form.html'
    success_url = reverse_lazy('link-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Link'
        context['button_label'] = 'Update Link'
        return context


class LinkDeleteView(DeleteView):
    model = Link
    template_name = 'linker/link_confirm_delete.html'
    success_url = reverse_lazy('link-list')
