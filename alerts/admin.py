from django.contrib import admin
from .models import Alert

# Register your models here.


class AlertAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'owner', 'timestamp',
                    'sensor', 'home', 'notes')

    def __init__(self, model, admin_site):
        super(AlertAdmin, self).__init__(model, admin_site)
        self.model = model

    def queryset(self, request):
        if request.user.is_superuser:
            return self.model.objects.all()
        return self.model.objects.filter(author=request.user)


admin.site.register(Alert, AlertAdmin)