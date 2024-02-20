from django.conf import settings
from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=100)
    # Assuming you want to keep a relation to track project observers
    observers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='supervised_projects'
    )

    def __str__(self):
        return self.name
