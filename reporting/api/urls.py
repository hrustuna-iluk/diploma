from django.conf.urls import patterns, include, url
#views
from reporting.api.Views.BenefitsView import BenefitsView
from reporting.api.Views.ClassView import ClassView
from reporting.api.Views.DepartmentView import DepartmentView
from reporting.api.Views.FacultyView import FacultyView
from reporting.api.Views.GroupView import GroupView
from reporting.api.Views.LanguageView import LanguageView
from reporting.api.Views.ParentsView import ParentsView
from reporting.api.Views.PublicPlanView import PublicPlanView
from reporting.api.Views.StudentView import StudentView
from reporting.api.Views.StudentWorkView import StudentWorkView
from reporting.api.Views.TeacherView import TeacherView
from reporting.api.Views.PassView import PassView


urlpatterns = patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),


    url(r'benefit/(?P<pk>[0-9]+)', BenefitsView.as_view()),
    url(r'benefit/$', BenefitsView.as_view()),
    url(r'benefits', BenefitsView.as_view()),

    url(r'class/(?P<pk>[0-9]+)', ClassView.as_view()),
    url(r'class/$', ClassView.as_view()),
    url(r'classes', ClassView.as_view()),

    url(r'department/(?P<pk>[0-9]+)', DepartmentView.as_view()),
    url(r'department/$', DepartmentView.as_view()),
    url(r'departments', DepartmentView.as_view()),

    url(r'faculty/', FacultyView.as_view()),
    url(r'faculties', FacultyView.as_view()),

    url(r'group/(?P<pk>[0-9]+)', GroupView.as_view()),
    url(r'group/$', GroupView.as_view()),
    url(r'groups', GroupView.as_view()),

    url(r'language/(?P<pk>[0-9]+)', LanguageView.as_view()),
    url(r'language/$', LanguageView.as_view()),
    url(r'languages', LanguageView.as_view()),

    url(r'parent/$', ParentsView.as_view()),
    url(r'parents', ParentsView.as_view()),

    url(r'publicplan/(?P<pk>[0-9]+)', PublicPlanView.as_view()),
    url(r'publicplan/$', PublicPlanView.as_view()),
    url(r'publicplans', PublicPlanView.as_view()),

    url(r'student/(?P<pk>[0-9]+)', StudentView.as_view()),
    url(r'student/$', StudentView.as_view()),
    url(r'students', StudentView.as_view()),

    url(r'studentwork/(?P<pk>[0-9]+)', StudentWorkView.as_view()),
    url(r'studentwork/$', StudentWorkView.as_view()),
    url(r'studentworks', StudentWorkView.as_view()),

    url(r'teacher/(?P<pk>[0-9]+)', TeacherView.as_view()),
    url(r'teacher/$', TeacherView.as_view()),
    url(r'teachers', TeacherView.as_view()),

    url(r'pass/(?P<pk>[0-9]+)', PassView.as_view()),
    url(r'pass/$', PassView.as_view()),
    url(r'passes', PassView.as_view())
)
