from reporting.models import Department, Pass, Group, Faculty, Student, Class, PASS_TYPES
import openpyxl
import os
from diplome.settings import BASE_DIR, STATIC_URL
from django.db.models import Count
from datetime import date


FILE_NAME_TEMPLATE = os.path.join(os.path.dirname(__file__), 'templates/')
FILE_NAME_DESTINATION = os.path.join(BASE_DIR, 'static', 'reductions/')
PASS_TYPES = [passType[0] for passType in PASS_TYPES]
START_LINE = 12
MONTHS = {
    '01': 'Січень',
    '02': 'Лютий',
    '03': 'Березень',
    '04': 'Квітень',
    '05': 'Травень',
    '06': 'Червень',
    '07': 'Липень',
    '08': 'Серпень',
    '09': 'Вересень',
    '10': 'Жовтень',
    '11': 'Листопад',
    '12': 'Грудень',
}


def generate_faculty_reduction_per_month(faculty, month, year):
    workbook = openpyxl.load_workbook(FILE_NAME_TEMPLATE + 'zvedenia2.xlsx')
    faculty = Faculty.objects.get(id=faculty)
    start_semester_date = faculty.startFirstSemester if int(month) >= 9 else faculty.startSecondSemester
    departments = Department.objects.all()
    group = Group.objects.all()
    ws = workbook.active

    ws['A4'] = 'факультету ' + faculty.title
    ws['A6'] = ' '.join(['за', MONTHS[month], str(year), 'навчального року'])

    start_index = START_LINE
    for index, department in enumerate(departments):
        start_index += 1
        groups = department.group_set.all()
        students = Student.objects.filter(group__id__in=groups)
        classes = Class.objects.filter(group__id__in=groups)
        all_passes = Pass.objects.filter(student__id__in=students, date__year=year, date__gte=start_semester_date, date__lt=date(int(year), int(month) + 1, 1))
        passes_by_type_pass = all_passes.filter(type='pass')
        passes_not_by_type_pass = all_passes.exclude(type='pass')
        ws['B' + str(start_index)] = department.title
        ws['C' + str(start_index)] = classes.count() * 2
        ws['D' + str(start_index)] = students.count()
        ws['E' + str(start_index)] = all_passes.distinct('student').count()
        ws['F' + str(start_index)] = ((all_passes.distinct('student').count() / students.count()) * 100) if students.count() > 0 else 0
        ws['G' + str(start_index)] = passes_by_type_pass.distinct('student').count()
        ws['H' + str(start_index)] = ((passes_by_type_pass.distinct('student').count() / students.count()) * 100) if students.count() > 0 else 0
        ws['I' + str(start_index)] = passes_by_type_pass.count() * 2
        ws['J' + str(start_index)] = all_passes.count() * 2
        ws['K' + str(start_index)] = ((passes_by_type_pass.count() / classes.count()) * 100) if classes.count() > 0 else 0
        ws['L' + str(start_index)] = ((all_passes.count() / classes.count()) * 100) if classes.count() > 0 else 0
        for curs in range(1, 5):
            start_index += 1
            groups = department.group_set.filter(yearStudy=curs)
            classes = Class.objects.filter(group__id__in=groups)
            students = Student.objects.filter(group__id__in=groups)
            all_passes = Pass.objects.filter(student__id__in=students, date__year=year, date__gte=start_semester_date, date__lt=date(int(year), int(month) + 1, 1))
            passes_by_type_pass = all_passes.filter(type='pass')
            passes_not_by_type_pass = all_passes.exclude(type='pass')
            ws['C' + str(start_index)] = classes.count() * 2
            ws['D' + str(start_index)] = students.count()
            ws['E' + str(start_index)] = all_passes.distinct('student').count()
            ws['F' + str(start_index)] = ((all_passes.distinct('student').count() / students.count()) * 100) if students.count() > 0 else 0
            ws['G' + str(start_index)] = passes_by_type_pass.distinct('student').count()
            ws['H' + str(start_index)] = ((passes_by_type_pass.distinct('student').count() / students.count()) * 100) if students.count() > 0 else 0
            ws['I' + str(start_index)] = passes_by_type_pass.count() * 2
            ws['J' + str(start_index)] = all_passes.count() * 2
            ws['K' + str(start_index)] = ((passes_by_type_pass.count() / classes.count()) * 100) if classes.count() > 0 else 0
            ws['L' + str(start_index)] = ((all_passes.count() / classes.count()) * 100) if classes.count() > 0 else 0

    workbook.save(FILE_NAME_DESTINATION + 'faculty_reduction_per_month.xlsx')
    return STATIC_URL + 'reductions/' + 'faculty_reduction_per_month.xlsx'


def generate_faculty_reduction_per_semester(faculty, semester, year):
    workbook = openpyxl.load_workbook(FILE_NAME_TEMPLATE + 'zvedenia2.xlsx')
    faculty = Faculty.objects.get(id=faculty)
    start_semester_date = faculty.startFirstSemester if int(semester) == 1 else faculty.startSecondSemester
    end_semester_date = faculty.endFirstSemester if int(semester) == 1 else faculty.endSecondSemester
    departments = Department.objects.all()
    group = Group.objects.all()
    ws = workbook.active

    ws['A4'] = 'факультету ' + faculty.title
    ws['A6'] = ' '.join(['за', semester, 'семестер', str(year), 'навчального року'])

    start_index = START_LINE
    for index, department in enumerate(departments):
        start_index += 1
        groups = department.group_set.all()
        students = Student.objects.filter(group__id__in=groups)
        classes = Class.objects.filter(group__id__in=groups, semester=semester)
        all_passes = Pass.objects.filter(student__id__in=students, date__year=year, date__gte=start_semester_date, date__lte=end_semester_date)
        passes_by_type_pass = all_passes.filter(type='pass')
        passes_not_by_type_pass = all_passes.exclude(type='pass')
        ws['B' + str(start_index)] = department.title
        ws['C' + str(start_index)] = classes.count() * 2
        ws['D' + str(start_index)] = students.count()
        ws['E' + str(start_index)] = all_passes.distinct('student').count()
        ws['F' + str(start_index)] = ((all_passes.distinct('student').count() / students.count()) * 100) if students.count() > 0 else 0
        ws['G' + str(start_index)] = passes_by_type_pass.distinct('student').count()
        ws['H' + str(start_index)] = ((passes_by_type_pass.distinct('student').count() / students.count()) * 100) if students.count() > 0 else 0
        ws['I' + str(start_index)] = passes_by_type_pass.count() * 2
        ws['J' + str(start_index)] = all_passes.count() * 2
        ws['K' + str(start_index)] = ((passes_by_type_pass.count() / classes.count()) * 100) if classes.count() > 0 else 0
        ws['L' + str(start_index)] = ((all_passes.count() / classes.count()) * 100) if classes.count() > 0 else 0
        for curs in range(1, 5):
            start_index += 1
            groups = department.group_set.filter(yearStudy=curs)
            classes = Class.objects.filter(group__id__in=groups, semester=semester)
            students = Student.objects.filter(group__id__in=groups)
            all_passes = Pass.objects.filter(student__id__in=students, date__year=year, date__gte=start_semester_date, date__lte=end_semester_date)
            passes_by_type_pass = all_passes.filter(type='pass')
            passes_not_by_type_pass = all_passes.exclude(type='pass')
            ws['C' + str(start_index)] = classes.count() * 2
            ws['D' + str(start_index)] = students.count()
            ws['E' + str(start_index)] = all_passes.distinct('student').count()
            ws['F' + str(start_index)] = ((all_passes.distinct('student').count() / students.count()) * 100) if students.count() > 0 else 0
            ws['G' + str(start_index)] = passes_by_type_pass.distinct('student').count()
            ws['H' + str(start_index)] = ((passes_by_type_pass.distinct('student').count() / students.count()) * 100) if students.count() > 0 else 0
            ws['I' + str(start_index)] = passes_by_type_pass.count() * 2
            ws['J' + str(start_index)] = all_passes.count() * 2
            ws['K' + str(start_index)] = ((passes_by_type_pass.count() / classes.count()) * 100) if classes.count() > 0 else 0
            ws['L' + str(start_index)] = ((all_passes.count() / classes.count()) * 100) if classes.count() > 0 else 0

    workbook.save(FILE_NAME_DESTINATION + 'faculty_reduction_per_semester.xlsx')
    return STATIC_URL + 'reductions/' + 'faculty_reduction_per_semester.xlsx'