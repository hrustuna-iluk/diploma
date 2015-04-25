from django.contrib.auth.models import Permission, User
from reporting.models import Teacher, Student
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout


PERMISSIONS = {
    'admin': Permission.objects.all(),
    'dean': None, #None value means that person can only browse
    'Deputy Dean': None,
    'Head of Department': None,
    'group_leader': Permission.objects.all(),
    'curator': Permission.objects.all()
}


def create_user(user_data):
    user = User.objects.create(
        username=user_data['username'],
        password=user_data['password'],
        email=user_data['email']
    )
    return user.save()


def get_person_by_user(user):
    person = None
    try:
        person = Student.objects.get(user=user)
    except Student.DoesNotExist:
        try:
            person = Teacher.objects.get(user=user)
        except Teacher.DoesNotExist:
            pass
    return person


def add_permission(user, role):
    user.user_permissions.clear()
    for permission in PERMISSIONS[role]:
        user.user_permissions.add(permission)
    return user


def get_permissions(user=None):
    if user:
        return Permission.objects.filter(user=user)
    else:
        return Permission.objects.all()
