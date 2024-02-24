from django.conf import settings
from django.db import models
from djf_surveys.models import Survey

LINK_PERIODICITY_CHOICES = (
    ('daily', 'daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('quarterly', 'Quarterly'),
    ('semester', 'Semester'),
    ('yearly', 'Yearly'),
)


class Link(models.Model):
    mentor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mentor_links',
        verbose_name='Mentor',
    )
    mentee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='mentee_links',
        verbose_name='Mentee',
    )
    mentor_survey = models.ForeignKey(
        Survey,
        on_delete=models.SET_NULL,
        related_name='mentor_surveys',
        null=True,
        blank=True,
        verbose_name='Mentor Survey',
    )
    mentee_survey = models.ForeignKey(
        Survey,
        on_delete=models.SET_NULL,
        related_name='mentee_surveys',
        null=True,
        blank=True,
        verbose_name='Mentee Survey',
    )
    periodicity = models.CharField(
        max_length=50,
        choices=LINK_PERIODICITY_CHOICES,
        default='weekly',  # Optional: Set a default value
        verbose_name='Periodicity',
    )
    times = models.IntegerField()

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return f'{self.person_one.username} <-> {self.person_two.username}'
