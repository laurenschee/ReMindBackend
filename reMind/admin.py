from django.contrib import admin
from .models import Home, Sensor, EmergencyContact

# Register your models here.


class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'owner', 'nickname')
    model = Home

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(HomeAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.owner.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return self.model.objects.all()
        return self.model.objects.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()


class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'arduino_id', 'created_at', 'owner', 'home', 'nickname')
    model = Sensor

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(SensorAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.owner.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return self.model.objects.all()
        return self.model.objects.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()


class EmergencyContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'owner', 'home',
                    'first_name', 'last_name', 'phone', 'email')
    model = EmergencyContact

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(EmergencyContactAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.owner.id:
            return False
        return True

    def queryset(self, request):
        if request.user.is_superuser:
            return self.model.objects.all()
        return self.model.objects.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()


admin.site.register(Home, HomeAdmin)
admin.site.register(Sensor, SensorAdmin)
admin.site.register(EmergencyContact, EmergencyContactAdmin)