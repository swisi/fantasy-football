from django.db import models
from nfldata.models import NFL_Players

class GameWeek(models.Model):
    week_number = models.IntegerField(unique=True)
    qb = models.ManyToManyField(NFL_Players, related_name='qb_selected', blank=True)
    rb = models.ManyToManyField(NFL_Players, related_name='rb_selected', blank=True)
    wr = models.ManyToManyField(NFL_Players, related_name='wr_selected', blank=True)
    te = models.ManyToManyField(NFL_Players, related_name='te_selected', blank=True)
    k = models.ManyToManyField(NFL_Players, related_name='k_selected', blank=True)
    qb_backup = models.ManyToManyField(NFL_Players, related_name='qb_backup_selected', blank=True)
    rb_backup = models.ManyToManyField(NFL_Players, related_name='rb_backup_selected', blank=True)
    wr_backup = models.ManyToManyField(NFL_Players, related_name='wr_backup_selected', blank=True)
    te_backup = models.ManyToManyField(NFL_Players, related_name='te_backup_selected', blank=True)
    k_backup = models.ManyToManyField(NFL_Players, related_name='k_backup_selected', blank=True)

    class Meta:
        ordering = ['week_number']
