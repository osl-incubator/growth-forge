from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import FeedbackForm, LinkForm, ProjectForm, UserRegistrationForm
from .models import Project


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(
                request,
                'registration/register_done.html',
                {'new_user': new_user},
            )
    else:
        user_form = UserRegistrationForm()
    return render(
        request, 'registration/register.html', {'user_form': user_form}
    )


@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project/list.html', {'projects': projects})


@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project/create.html', {'form': form})


# Define similar views for Link and Feedback


@login_required
def link_create(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('link_list')
    else:
        form = LinkForm()
    return render(request, 'link/create.html', {'form': form})


@login_required
def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/create.html', {'form': form})


# Add views for listing Links and Feedbacks, and any other operations you need
