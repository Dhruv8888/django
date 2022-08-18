from django.contrib import admin

from add_employee.models import device

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('Id', 'DeviceType', 'DeviceVersion', 'DeviceLocation', 'PrimaryGroup', 'SecondaryGroup', 'LastContact', 'Status')

    # def __str__(self):
    #     return "{}:{}..".format(self.id, self.paragraph[:10])


admin.site.register(device, ServiceAdmin)
# Register your models here.
