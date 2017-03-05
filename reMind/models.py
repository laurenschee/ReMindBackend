from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Home(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    owner = models.ForeignKey('auth.User', related_name='homes')
    nickname = models.CharField(editable=True, max_length=128, unique=True, default="My Home")

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Home, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)


class Sensor(models.Model):
    arduino_id = models.CharField(max_length=128, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    owner = models.ForeignKey('auth.User', related_name='sensors')
    home = models.ForeignKey(Home, related_name='sensors')
    nickname = models.CharField(editable=True, max_length=128, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Sensor, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)


class EmergencyContact(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    owner = models.ForeignKey('auth.User', related_name='set_emergency_contacs')
    home = models.ForeignKey(Home, related_name='emergency_contacts')
    first_name = models.CharField(editable=True, max_length=128, unique=True)
    last_name = models.CharField(editable=True, max_length=128, unique=True)
    phone = models.CharField(editable=True, max_length=128, unique=True)
    email = models.CharField(editable=True, max_length=128, unique=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(EmergencyContact, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)