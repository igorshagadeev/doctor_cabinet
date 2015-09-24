# django
from django.contrib import admin

# project
from doctor.models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Doctor, DoctorAdmin)








