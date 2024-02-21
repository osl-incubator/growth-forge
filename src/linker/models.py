from django.conf import settings
from django.db import models

LINK_PERIODICITY_CHOICES = (
    ('daily', 'daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('quarterly', 'Quarterly'),
    ('semester', 'Semester'),
    ('yearly', 'Yearly'),
)


class Link(models.Model):
    person_one = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='person_one_links',
    )
    person_two = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='person_two_links',
    )
    supervisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='supervised_links',
    )
    periodicity = models.CharField(max_length=50)
    times = models.IntegerField()

    def __str__(self):
        return f'{self.person_one.username} <-> {self.person_two.username}'
