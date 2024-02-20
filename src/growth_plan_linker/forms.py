from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Feedback, Link, Profile, Project


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # Add any additional fields for the profile here, if needed

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    # Add fields for updating profile-specific information
    class Meta:
        model = Profile
        fields = []  # Specify the fields you want to include, e.g., []


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'supervisors',
        ]  # Adjust according to your Project model fields


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
                choices=Link.PERIODICITY_CHOICES,
                attrs={'class': 'form-control'},
            ),
            'times': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content', 'link']
        widgets = {
            'content': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
            'link': forms.Select(attrs={'class': 'form-control'}),
        }
