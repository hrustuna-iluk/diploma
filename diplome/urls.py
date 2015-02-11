from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^app/', include('reporting.urls')),
    url(r'^api/', include('reporting.api.urls')),
    url(r'^admin/', include(admin.site.urls))
)

