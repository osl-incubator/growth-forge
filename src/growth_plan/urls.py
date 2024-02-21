from django.urls import path

from .views import (
    GrowthPlanItemCreateView,
    GrowthPlanItemDeleteView,
    GrowthPlanItemUpdateView,
    review_growth_plan_list,
    user_growth_plan_list,
)

urlpatterns = [
    path(
        'my-growth-plan/', user_growth_plan_list, name='user-growth-plan-list'
    ),
    path(
        'review-growth-plans/',
        review_growth_plan_list,
        name='review-growth-plan-list',
    ),
    path(
        'create/',
        GrowthPlanItemCreateView.as_view(),
        name='growth-plan-item-create',
    ),
    path(
        'edit/<int:pk>/',
        GrowthPlanItemUpdateView.as_view(),
        name='growth-plan-item-edit',
    ),
    path(
        'delete/<int:pk>/',
        GrowthPlanItemDeleteView.as_view(),
        name='growth-plan-item-delete',
    ),
]
