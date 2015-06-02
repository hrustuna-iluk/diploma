from django.http import *
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from reporting.excel_generator.group_reduction_excel_generator import generate_group_reduction
from reporting.excel_generator.faculty_reduction_excel_generator import generate_faculty_reduction_per_month, generate_faculty_reduction_per_semester
from reporting.excel_generator.journal_excel_generator import generate_journal_excel
import json
from datetime import date
from django.core.mail import send_mail, BadHeaderError
from diplome.settings import EMAIL_HOST_USER
from reporting.models import Group, Department, Class, Pass


@login_required(login_url=reverse_lazy('login_user'))
def index(request):
    role = ''
    if request.user.student_set.all().first():
        role = 'student'
    elif request.user.teacher_set.all().first():
        role = request.user.teacher_set.all().first().position
    elif request.user.is_superuser:
        role = 'admin'
    return render_to_response('index.html', {'request': request, 'role': role}, context_instance = RequestContext(request))


def login_user(request):
    logout(request)
    username = password = ''
    start_page = '#'
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.student_set and user.student_set.all().first():
                persona = user.student_set.all().first()
                group = Group.objects.filter(leader=persona)
                if group.count():
                    start_page += 'reduction/' + str(group.first().id)
            elif user.teacher_set and user.teacher_set.all().first():
                persona = user.teacher_set.all().first()
                if persona.position == 'Head of Department':
                    department = Department.objects.filter(headOfDepartment=persona)
                    if department.count():
                        start_page += 'groups/' + str(department.first().id)
                elif persona.position == 'teacher':
                    group = Group.objects.filter(curator=persona)
                    if group.count():
                        start_page += 'reduction/' + str(group.first().id)
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('index') + start_page)
    return render_to_response('login.html', context_instance=RequestContext(request))


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('login_user'))


@login_required
def generate_reduction(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('data'))
        filename = None
        type = data.get('type')
        faculty = data.get('faculty')

        if type == 'groupPerMonth':
            group = data.get('group')
            year, month = data.get('month').split('-')
            filename = generate_group_reduction(faculty, group, month, year)
        elif type == 'facultyPerMonth':
            year, month = data.get('month').split('-')
            filename = generate_faculty_reduction_per_month(faculty, month, year, data)
        elif type == 'facultyPerSemester':
            semester = data.get('semester')
            year = data.get('year')
            filename = generate_faculty_reduction_per_semester(faculty, semester, year, data)
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
    return HttpResponseBadRequest()

@login_required
def delete_schedule(request):
    if request.method == 'POST':
        group = request.POST.get('group')
        Class.objects.filter(group__id=group).delete()
        return HttpResponse(json.dumps({'message': 'Розклад видалено'}), content_type='application/json')
    return HttpResponse(json.dumps({'message': 'Розклад не видалено'}), content_type='application/json')


@login_required
def delete_passes(request):
    if request.method == 'POST':
        Pass.objects.all().delete()
        return HttpResponse(json.dumps({'message': 'Пропуски видалено'}), content_type='application/json')
    return HttpResponse(json.dumps({'message': 'Пропуски не видалено'}), content_type='application/json')


@login_required
def generate_journal(request):
    if request.method == 'POST':
        group = request.POST.get('group')
        filename = generate_journal_excel(group)
        return HttpResponse(json.dumps({'url': filename}), content_type='application/json')
    return HttpResponseBadRequest()