from django.conf.urls import patterns, include, url
from reporting.views import index, login_user, logout_user, generate_reduction, generate_journal, send_email, delete_schedule, delete_passes

urlpatterns = patterns('',
    url(r'reduction/$', generate_reduction, name='generate_reduction'),
    url(r'journal/$', generate_journal, name='generate_journal'),
    url(r'send_mail/$', send_email, name='send_mail'),
    url(r'deleteSchedule/$', delete_schedule, name='delete_schedule'),
    url(r'deletePasses/$', delete_passes, name='delete_passes'),
    url(r'reporting/$', index, name='index'),
    url(r'login/$', login_user, name='login_user'),
    url(r'logout/$', logout_user, name='logout_user')
)
