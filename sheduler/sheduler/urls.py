"""sheduler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
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

if  settings.DEBUG:
    #print(settings.STATICFILES_DIRS)
    urlpatterns += patterns('',
        (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}), 
    )
    urlpatterns +=  patterns(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
    pass
else:
    pass