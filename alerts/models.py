from __future__ import unicode_literals

from django.db import models
from reMind import models as homesense_models
from django.utils import timezone

# Create your models here.


class Alert(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    owner = models.ForeignKey('auth.User', related_name='alerts')
    timestamp = models.DateTimeField(null=True, blank=True)
    sensor = models.ForeignKey(homesense_models.Sensor, related_name='sensor_alerts')
    home = models.ForeignKey(homesense_models.Home, related_name='home_alerts')
    notes = models.CharField(max_length=1024, null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Alert, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)
        # permissions = (
        #     ('readonly', 'Can Read Only Cars')
        # )