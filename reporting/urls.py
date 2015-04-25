from django.conf.urls import patterns, include, url
from reporting.views import index, login_user, logout_user, generate_reduction

urlpatterns = patterns('',
    url(r'reduction/$', generate_reduction, name='generate_reduction'),
    url(r'reporting/$', index, name='index'),
    url(r'login/$', login_user, name='login_user'),
    url(r'logout/$', logout_user, name='logout_user')
)
