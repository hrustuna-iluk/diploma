from reporting.models import Group, Department, Student, Teacher
from reporting.manage_users import get_person_by_user
from django.http import HttpResponseForbidden


DEPARTMENT_SCREENS = [
    'teachers',
    'groups'
]

GROUP_SCREENS = [
    'students'
    'reduction',
    'scheduler',
    'journal',
    'publicOrders'
]


class CheckPermission(object):

    def process_request(self, request):
        if request.user.is_authenticated() and not request.user.is_superuser:
            params = request.GET
            screen = params.get('screen')
            user = get_person_by_user(request.user)
            request.session['permission_denied'] = False

            if user and screen:
                department = None
                group = None
                if screen == 'departments':
                    if isinstance(user, Teacher):
                        if user.position != 'dean' or user.position != 'Deputy Dean':
                            request.session['permission_denied'] = True
                    else:
                        request.session['permission_denied'] = True
                elif screen in DEPARTMENT_SCREENS:
                    try:
                        department = Department.objects.get(id=params.get('department'))
                    except Department.DoesNotExist:
                        request.session['permission_denied'] = True
                        return
                    if isinstance(user, Teacher):
                        if user.position in ['dean', 'Deputy Dean']:
                            pass
                        elif user.position == 'Head of Department':
                            if not department.headOfDepartment or user.id != department.headOfDepartment.id:
                                request.session['permission_denied'] = True
                        else:
                            request.session['permission_denied'] = True
                    else:
                        request.session['permission_denied'] = True
                    request.session['department'] = department.id
                elif screen in GROUP_SCREENS:
                    try:
                        group = Group.objects.get(id=params.get('group'))
                    except Group.DoesNotExist:
                        request.session['permission_denied'] = True
                        return
                    if 'department' in request.session and request.session['department'] == group.department.id:
                        request.session['permission_denied'] = False
                        return
                    if isinstance(user, Student):
                        if user.id != group.leader.id:
                            request.session['permission_denied'] = True
                    elif isinstance(user, Teacher):
                        if user.id != group.curator.id:
                            request.session['permission_denied'] = True

    def process_response(self, request, response):
        try:
            if request.session['permission_denied']:
                request.session['permission_denied'] = False
                return HttpResponseForbidden()
        except KeyError:
            return response
        return response