from django.conf.urls import patterns, include, url
from reporting.views import index, login_user, logout_user


urlpatterns = patterns('',
    url(r'reporting/$', index, name='index'),
    url(r'login/$', login_user, name='login_user'),
    url(r'logout/$', logout_user, name='logout_user')
)
