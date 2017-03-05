from django.contrib import admin
from .models import EmergencyContact

# Register your models here.


class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'home', 'first_name', 'last_name', 'phone', 'email')


admin.site.register(EmergencyContact, EmergencyContactAdmin)