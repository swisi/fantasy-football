from django.db import models
from nfldata.models import NFL_Players

class GamePlay(models.Model):
    week_number = models.IntegerField()
    qb = models.ForeignKey(NFL_Players, related_name='qb_selected', on_delete=models.SET_NULL, null=True, blank=True)
    rb = models.ForeignKey(NFL_Players, related_name='rb_selected', on_delete=models.SET_NULL, null=True, blank=True)
    wr = models.ForeignKey(NFL_Players, related_name='wr_selected', on_delete=models.SET_NULL, null=True, blank=True)
    te = models.ForeignKey(NFL_Players, related_name='te_selected', on_delete=models.SET_NULL, null=True, blank=True)
    k = models.ForeignKey(NFL_Players, related_name='k_selected', on_delete=models.SET_NULL, null=True, blank=True)
    qb_backup = models.ForeignKey(NFL_Players, related_name='qb_backup_selected', on_delete=models.SET_NULL, null=True, blank=True)
    rb_backup = models.ForeignKey(NFL_Players, related_name='rb_backup_selected', on_delete=models.SET_NULL, null=True, blank=True)
    wr_backup = models.ForeignKey(NFL_Players, related_name='wr_backup_selected', on_delete=models.SET_NULL, null=True, blank=True)
    te_backup = models.ForeignKey(NFL_Players, related_name='te_backup_selected', on_delete=models.SET_NULL, null=True, blank=True)
    k_backup = models.ForeignKey(NFL_Players, related_name='k_backup_selected', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('week_number',)
        ordering = ['week_number']

