from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from growth_forge.utils import ignore_vulture_issue


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    projects = models.ManyToManyField(
        'projects.Project', related_name='participants'
    )

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    ignore_vulture_issue(sender, created, **kwargs)
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
