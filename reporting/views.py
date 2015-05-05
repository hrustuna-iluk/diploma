from django.http import *
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from reporting.excel_generator.group_reduction_excel_generator import generate_group_reduction
from reporting.excel_generator.faculty_reduction_excel_generator import generate_faculty_reduction_per_month, generate_faculty_reduction_per_semester
import json
from datetime import date
from django.core.mail import send_mail, BadHeaderError
from diplome.settings import EMAIL_HOST_USER


@login_required(login_url=reverse_lazy('login_user'))
def index(request):
    return render_to_response('index.html', {'request': request}, context_instance = RequestContext(request))


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('index'))
    return render_to_response('login.html', context_instance=RequestContext(request))

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login_user'))


@login_required
def generate_reduction(request):
    if request.method == 'POST':
        filename = None
        type = request.POST.get('type')
        faculty = request.POST.get('faculty')

        if type == 'groupPerMonth':
            group = request.POST.get('group')
            year, month = request.POST.get('month').split('-')
            filename = generate_group_reduction(faculty, group, month, year)
        elif type == 'facultyPerMonth':
            year, month = request.POST.get('month').split('-')
            filename = generate_faculty_reduction_per_month(faculty, month, year)
        elif type == 'facultyPerSemester':
            semester = request.POST.get('semester')
            year = request.POST.get('year')
            filename = generate_faculty_reduction_per_semester(faculty, semester, year)
    return HttpResponse(json.dumps({'url': filename}), content_type='application/json')


def send_email(request):
    if request.method == 'POST':
        from reporting.models import Student
        student = Student.objects.get(id=request.POST.get('student'))
        subject = 'Перевищено ліміт пропусків'
        message = request.POST.get('message')
        try:
            send_mail(subject, message, EMAIL_HOST_USER, [student.email])
        except BadHeaderError:
            return HttpResponse(json.dumps({'error': 'Invalid header found.'}), content_type='application/json')
        return HttpResponse(json.dumps({'success': True}), content_type='application/json')
    return  HttpResponseBadRequest()