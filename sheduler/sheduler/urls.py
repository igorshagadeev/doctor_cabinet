from django.conf.urls import include, url, patterns
from django.contrib import admin

from sheduler.views import (main, get_doctor_shedule, save_appointment)

urlpatterns = [

    url(r'^$', main),
    url(r'^get_doctor_shedule$', get_doctor_shedule),
    url(r'^save_appointment$', save_appointment),

    url(r'^admin/', include(admin.site.urls)),
]



from sheduler import settings
from django.conf.urls.static import static

if settings.DEBUG:
    # print(settings.STATICFILES_DIRS)
    urlpatterns += patterns('',
        (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
    urlpatterns += patterns(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    pass
else:
    pass
