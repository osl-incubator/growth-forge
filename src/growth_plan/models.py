from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class GrowthPlanItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='growth_plan_items',
        verbose_name=_('User'),
    )
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.TextField(verbose_name=_('Description'))
    start_date = models.DateField(verbose_name=_('Start Date'))
    end_date = models.DateField(verbose_name=_('End Date'))
    progress_percentage = models.PositiveIntegerField(
        default=0,
        verbose_name=_('Progress Percentage'),
        help_text=_('Enter a number between 0 and 100.'),
    )

    class Meta:
        verbose_name = _('Growth Plan Item')
        verbose_name_plural = _('Growth Plan Items')

    def __str__(self):
        return self.title
