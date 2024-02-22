from django import forms
from django.contrib.auth import get_user_model
from djf_surveys.models import Survey

from .models import LINK_PERIODICITY_CHOICES, Link

User = get_user_model()


class LinkForm(forms.ModelForm):
    mentor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Mentor',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    mentee = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Mentee',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    mentor_survey = forms.ModelChoiceField(
        queryset=Survey.objects.all(),
        label='Mentor Survey',
        required=False,  # Making survey selection optional
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    mentee_survey = forms.ModelChoiceField(
        queryset=Survey.objects.all(),
        label='Mentee Survey',
        required=False,  # Making survey selection optional
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    periodicity = forms.ChoiceField(
        choices=LINK_PERIODICITY_CHOICES,
        label='Periodicity',
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    times = forms.IntegerField(
        label='Times',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        min_value=1,  # Assuming 'times' cannot be less than 1
    )

    class Meta:
        model = Link
        fields = [
            'mentor',
            'mentee',
            'mentor_survey',
            'mentee_survey',
            'periodicity',
            'times',
        ]
