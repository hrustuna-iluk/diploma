from reporting.models import *
import openpyxl
import os
from diplome.settings import BASE_DIR, STATIC_URL


FILE_NAME_TEMPLATE = os.path.join(os.path.dirname(__file__), 'templates/')
FILE_NAME_DESTINATION = os.path.join(BASE_DIR, 'static', 'reductions/')
PASS_TYPES = [passType[0] for passType in PASS_TYPES]
MARITAL_STATUSES = {
    'single': 'Не одружений',
    'married': 'Одружений'
}

def generate_journal_excel(group):
    sheets = {
        'а) Обгортка': fill_start_page,
        'б) Розподіл громад. доручень': fill_public_orders,
        'в) Відомості': fill_news,
        'в2) Інформація для мене': fill_info_for_me,
        'г) План громадсько-вих. роботи': fill_plan,
        'д) Облік відвідувань': fill_accounting,
        'е) Громад.-Вих. заходи': fill_public_attitude,
        'ж) Індивід. робота з студентами': fill_individual_work,
        'з) Звіт про гром.-вих. роботу': fill_report
    }
    workbook = openpyxl.load_workbook(FILE_NAME_TEMPLATE + 'journal.xlsx')
    group = Group.objects.get(id=group)
    students = Student.objects.filter(group=group)

    for sheet in sheets:
        ws = workbook.get_sheet_by_name(sheet)
        sheets[sheet](ws, group)

    workbook.save(FILE_NAME_DESTINATION + 'journal.xlsx')
    return STATIC_URL + 'reductions/' + 'journal.xlsx'


def fill_start_page(ws, group):
    ws['B6'] = ' '.join(['Факультет:', group.department.title])
    ws['B7'] = ' '.join(['Куратор:', group.curator.lastName, group.curator.firstName, group.curator.middleName])
    ws['B8'] = ' '.join(['Староста:', group.leader.lastName, group.leader.firstName])


def fill_public_orders(ws, group):
    ws['A2'] = '1.Курс'
    ws['B2'] = group.yearStudy
    ws['A3'] = '2.Група'
    ws['B3'] = group.number
    ws['A4'] = '3.Староста'
    ws['B4'] = group.leader.lastName + ' ' + group.leader.firstName if group.leader else ''
    ws['A5'] = '4.Заступник старости'
    ws['B5'] = group.deputyHeadman.lastName + ' ' + group.deputyHeadman.firstName if group.deputyHeadman else ''
    ws['A6'] = '5.Профгрупорг'
    ws['B6'] = group.organizer.lastName + ' ' + group.organizer.firstName if group.organizer else ''
    ws['A7'] = '6.Культурно-дозвіллєва робота'
    ws['B7'] = group.culturalWork.lastName + ' ' + group.culturalWork.firstName if group.culturalWork else ''
    ws['A8'] = '7.Спортивно-оздоровча робота'
    ws['B8'] = group.healthWork.lastName + ' ' + group.healthWork.firstName if group.healthWork else ''
    ws['A9'] = '8.Редколегія'
    start_index = 9
    for person in group.editorialBoard.all():
        ws['B' + str(start_index)] = person.lastName + ' ' + person.firstName
        start_index += 1
    ws['A' + str(start_index)] = '9.Інші доручення'
    for person in group.otherTasks.all():
        ws['B' + str(start_index)] = person.lastName + ' ' + person.firstName
        start_index += 1


def fill_news(ws, group):
    students = group.student_set.all()
    start_index = 4
    for index, student in enumerate(students):
        ws['A' + str(start_index)] = index + 1
        ws['B' + str(start_index)] = ' '.join([student.lastName, student.firstName, student.middleName])
        ws['C' + str(start_index)] = student.dateBirth
        ws['D' + str(start_index)] = student.nationality or '~'
        ws['E' + str(start_index)] = MARITAL_STATUSES[student.maritalStatus]
        ws['F' + str(start_index)] = student.id
        ws['G' + str(start_index)] = ' '.join([student.address, 'тел.', student.phone])
        ws['H' + str(start_index)] = ' '.join([student.father.fullName, student.father.position + ',', student.mother.fullName, student.mother.position ])


def fill_info_for_me(ws, group):
    students = group.student_set.all()
    ws['A1'] = group.number
    start_index = 3
    for index, student in enumerate(students):
        ws['A' + str(start_index)] = index + 1
        ws['B' + str(start_index)] = ' '.join([student.lastName, student.firstName, student.middleName])
        ws['C' + str(start_index)] = student.additional
        ws['D' + str(start_index)] = ''
        ws['E' + str(start_index)] = student.phone
        ws['F' + str(start_index)] = student.email
        ws['G' + str(start_index)] = student.address
        ws['H' + str(start_index)] = '\n'.join([student.father.phone, student.mother.phone])
        ws['I' + str(start_index)] = ''
        ws['J' + str(start_index)] = student.school


def fill_plan(ws, group):
    pass


def fill_accounting(ws, group):
    pass


def fill_public_attitude(ws, group):
    pass


def fill_individual_work(ws, group):
    pass


def fill_report(ws, group):
    pass



