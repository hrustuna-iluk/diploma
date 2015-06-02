from reporting.models import *
import openpyxl
import os
from diplome.settings import BASE_DIR, STATIC_URL


FILE_NAME_TEMPLATE = os.path.join(os.path.dirname(__file__), 'templates/')
FILE_NAME_DESTINATION = os.path.join(BASE_DIR, 'static', 'reductions/')
PASS_TYPES = [passType[0] for passType in PASS_TYPES]


def generate_journal_excel(group):
    workbook = openpyxl.load_workbook(FILE_NAME_TEMPLATE + 'journal.xlsx')
    group = Group.objects.get(id=group)
    students = Student.objects.filter(group=group)
    ws = workbook.active

    workbook.save(FILE_NAME_DESTINATION + 'journal.xlsx')
    return STATIC_URL + 'reductions/' + 'journal.xlsx'
