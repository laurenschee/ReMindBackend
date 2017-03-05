from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Home(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    owner = models.ForeignKey('auth.User', related_name='homes')
    nickname = models.CharField(editable=False, max_length=128, unique=True, default="My Home")

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
    home = models.ForeignKey(Home, related_name='sensors')
    nickname = models.CharField(editable=False, max_length=128, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Sensor, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)


class Alert(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    timestamp = models.DateTimeField(null=True, blank=True)
    sensor = models.ForeignKey(Home, related_name='sensor_alerts')
    home = models.ForeignKey(Home, related_name='home_alerts')
    notes = models.CharField(max_length=1024, null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Alert, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)


class EmergencyContact(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)
    home = models.ForeignKey(Home, related_name='emergency_contacts')
    first_name = models.CharField(editable=False, max_length=128, unique=True)
    last_name = models.CharField(editable=False, max_length=128, unique=True)
    phone = models.CharField(editable=False, max_length=128, unique=True)
    email = models.CharField(editable=False, max_length=128, unique=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(EmergencyContact, self).save(*args, **kwargs)

    class Meta:
        ordering = ('created_at',)