from reporting.models import Student, Pass
import openpyxl
import os
from diplome.settings import BASE_DIR, STATIC_URL

FILE_NAME_TEMPLATE = os.path.join(os.path.dirname(__file__), 'templates/')
FILE_NAME_DESTINATION = os.path.join(BASE_DIR, 'static', 'reductions/')


def generate_group_reduction_per_month(group, month, year):
    workbook = openpyxl.load_workbook(FILE_NAME_TEMPLATE + 'zvedenia1.xlsx')
    ws = workbook.active

    workbook.save(FILE_NAME_DESTINATION + 'test.xlsx')
    return STATIC_URL + 'reductions/' + 'test.xlsx'


def generate_faculty_reduction_per_month(faculty, month, year):
    pass


def generate_faculty_reduction_per_semester(faculty, semester):
    pass