from django.contrib.auth.models import Permission, User
from reporting.models import Teacher, Student
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout


def create_user(request, person_data):
    user = User.objects.create(
        usename=person_data.username,
        password=person_data.password,
        email=person_data.email
    )
    user.save()
    return user


def get_person_by_user(user, person_type):
    person = None
    try:
        if person_type == 'student':
            person = Student.objects.get(user=user)
        elif person_type == 'teacher':
            person = Teacher.objects.get(user=user)
    except (Teacher.DoesNotExist, Student.DoesNotExist):
        pass
    return person


def add_permission(user, permission_list):
    user.user_permissions.clear()
    for permission in permission_list:
        user.user_permissions.add(permission)
    return user

def get_permissions(user=None):
    if user:
        return Permission.objects.filter(user=user)
    else:
        return Permission.objects.all()
