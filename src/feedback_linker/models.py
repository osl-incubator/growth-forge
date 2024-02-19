from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    projects = models.ManyToManyField('Project', related_name='participants')
    # Add any additional fields for your Person model here

    def __str__(self):
        return self.user.username


class Project(models.Model):
    name = models.CharField(max_length=100)
    # Assuming you want to keep a relation to track project supervisors
    supervisors = models.ManyToManyField(
        User, related_name='supervised_projects'
    )

    def __str__(self):
        return self.name


class Link(models.Model):
    person_one = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='person_one_links'
    )
    person_two = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='person_two_links'
    )
    supervisor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='supervised_links'
    )
    periodicity = models.CharField(max_length=50)
    times = models.IntegerField()

    def __str__(self):
        return f'{self.person_one.username} <-> {self.person_two.username}'


class Feedback(models.Model):
    content = models.TextField()
    link = models.ForeignKey(
        Link, on_delete=models.CASCADE, related_name='feedback'
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f'Feedback from {self.link.person_one.username} to '
            f'{self.link.person_two.username} on '
            f'{self.timestamp.strftime("%Y-%m-%d %H:%M:%S")}'
        )


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
