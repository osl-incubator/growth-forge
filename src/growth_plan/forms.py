from django import forms
from django.conf import settings

from .models import GrowthPlanItem


class GrowthPlanItemForm(forms.ModelForm):
    class Meta:
        model = GrowthPlanItem
        fields = [
            'title',
            'description',
            'start_date',
            'end_date',
            'progress_percentage',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(
                format=[settings.DATE_INPUT_FORMATS[0]],
                attrs={'class': 'form-control', 'type': 'date'},
            ),
            'end_date': forms.DateInput(
                format=[settings.DATE_INPUT_FORMATS[0]],
                attrs={'class': 'form-control', 'type': 'date'},
            ),
            'progress_percentage': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
        }
