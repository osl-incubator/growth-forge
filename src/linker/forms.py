from django import forms

from .models import LINK_PERIODICITY_CHOICES, Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = [
            'person_one',
            'person_two',
            'supervisor',
            'periodicity',
            'times',
        ]
        widgets = {
            'person_one': forms.Select(attrs={'class': 'form-control'}),
            'person_two': forms.Select(attrs={'class': 'form-control'}),
            'supervisor': forms.Select(attrs={'class': 'form-control'}),
            'periodicity': forms.Select(
                choices=LINK_PERIODICITY_CHOICES,
                attrs={'class': 'form-control'},
            ),
            'times': forms.NumberInput(attrs={'class': 'form-control'}),
        }
