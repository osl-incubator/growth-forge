from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DeleteView, UpdateView
from django.views.generic.edit import CreateView

from .forms import GrowthPlanItemForm
from .models import GrowthPlanItem


@login_required
def user_growth_plan_list(request):
    # List only the logged-in user's growth plan items
    items = GrowthPlanItem.objects.filter(user=request.user)
    return render(request, 'my-growth-plan.html', {'items': items})


@login_required
def review_growth_plan_list(request):
    # Accessible only to supervisors; list users' growth
    # plan items linked through projects
    if not request.user.supervised_projects.exists():
        return HttpResponseForbidden()
    supervised_users = User.objects.filter(
        projects__supervisors=request.user
    ).distinct()
    items = GrowthPlanItem.objects.filter(
        user__in=supervised_users
    ).select_related('user')
    return render(request, 'review-growth-plan-list.html', {'items': items})


@method_decorator(login_required, name='dispatch')
class GrowthPlanItemCreateView(CreateView):
    model = GrowthPlanItem
    form_class = GrowthPlanItemForm
    template_name = 'growth-plan-item-form.html'

    def form_valid(self, form):
        form.instance.user = (
            self.request.user
        )  # Set the user to the current user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'user-growth-plan-list'
        )  # Redirect to the user's growth plan list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context


class GrowthPlanItemUpdateView(UpdateView):
    model = GrowthPlanItem
    form_class = GrowthPlanItemForm
    template_name = 'growth-plan-item-form.html'
    success_url = reverse_lazy('user-growth-plan-list')

    def get_queryset(self):
        # Users can only edit their own growth plan items
        return GrowthPlanItem.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit'
        return context


class GrowthPlanItemDeleteView(DeleteView):
    model = GrowthPlanItem
    template_name = 'growth-plan-item-confirm-delete.html'
    success_url = reverse_lazy('user-growth-plan-list')

    def get_queryset(self):
        # Users can only delete their own growth plan items
        return GrowthPlanItem.objects.filter(user=self.request.user)
