from django.conf.urls import patterns, include, url
#views
from reporting.api.Views.AdditionalView import AdditionalView
from reporting.api.Views.BenefitsView import BenefitsView
from reporting.api.Views.ClassRoomView import ClassRoomView
from reporting.api.Views.ClassView import ClassView
from reporting.api.Views.DepartmentView import DepartmentView
from reporting.api.Views.EventView import EventView
from reporting.api.Views.FacultyView import FacultyView
from reporting.api.Views.GroupView import GroupView
from reporting.api.Views.LanguageView import LanguageView
from reporting.api.Views.ParentsView import ParentsView
from reporting.api.Views.PublicPlanView import PublicPlanView
from reporting.api.Views.ReportView import ReportView
from reporting.api.Views.StudentView import StudentView
from reporting.api.Views.StudentWorkView import StudentWorkView
from reporting.api.Views.SubjectView import SubjectView
from reporting.api.Views.TeacherView import TeacherView



urlpatterns = patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^additional|additionals/(?P<pk>\d+)', AdditionalView.as_view()),
    url(r'^benefit|benefits/(?P<pk>\d+)', BenefitsView.as_view()),
    url(r'^classroom|classrooms/(?P<pk>\d+)', ClassRoomView.as_view()),
    url(r'^class|classes/(?P<pk>\d+)', ClassView.as_view()),
    url(r'^department|departments/(?P<pk>\d+)', DepartmentView.as_view()),
    url(r'^event|events/(?P<pk>\d+)', EventView.as_view()),
    url(r'^faculty|faculties/(?P<pk>\d+)', FacultyView.as_view()),
    url(r'^group|groups/(?P<pk>\d+)', GroupView.as_view()),
    url(r'^language|languages/(?P<pk>\d+)', LanguageView.as_view()),
    url(r'^parent|parents/(?P<pk>\d+)', ParentsView.as_view()),
    url(r'^publicplan|publicplans/(?P<pk>\d+)', PublicPlanView.as_view()),
    url(r'^report|reports/(?P<pk>\d+)', ReportView.as_view()),
    url(r'^student|students/(?P<pk>\d+)', StudentView.as_view()),
    url(r'^studentwork|studentworks/(?P<pk>\d+)', StudentWorkView.as_view()),
    url(r'^subject|subjects/(?P<pk>\d+)', SubjectView.as_view()),
    url(r'^teacher|teachers/(?P<pk>\d+)', TeacherView.as_view())
)
