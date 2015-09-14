from django.contrib import admin

# Register your models here.






from doctor.models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    pass


admin.site.register( Doctor, DoctorAdmin)








