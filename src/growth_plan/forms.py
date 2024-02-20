from django import forms

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
            # Specify the date format for start_date and end_date fields
            'start_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'},
            ),
            'end_date': forms.DateInput(
                format='%Y-%m-%d',
                attrs={'class': 'form-control', 'type': 'date'},
            ),
            'progress_percentage': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
        }
