#-*-coding:UTF-8-*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

POSITIONS = (
    ('dean', 'Декан'),
    ('Head of Department', 'Завідувач кафедри'),
    ('teacher', 'Викладач')
)

MARITAL_STATUSES = (
    ('single', 'Не одружений'),
    ('married', 'Одружений')
)

SEX = (
    ('male', 'Чоловіча'),
    ('female', 'Жіноча'),
)

SUBJECT_TYPES = (
    ('lection', 'Лекція'),
    ('practic', 'Практика'),
    ('lab', 'Лабораторний практикум')
)

TUITION_TYPES = (
    ('stationary', 'Стаціонар'),
    ('extramural', 'Заочна форма'),
)

DAYS = (
    ('monday', 'Понеділок'),
    ('tuesday', 'Вівторок'),
    ('wednesday', 'Середа'),
    ('Thursday', 'Четвер'),
    ('Friday', "П'ятниця"),
    ('Saturday', 'Субота'),
    ('Sunday', 'Неділя')
)

PASS_TYPES = (
    ('pass', "Без поважної причини"),
    ('sickness', "По хворобі"),
    ('statement', "За'ява"),
    ('watch', "Чергування"),
)

class Faculty(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Department(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Group(models.Model):
    number = models.CharField(max_length=25)
    department = models.ForeignKey(Department)
    leader = models.ForeignKey('Student', related_name='gr_lead')
    yearStudy = models.IntegerField()
    tuition = models.CharField(max_length=50, choices=TUITION_TYPES)
    curator = models.ForeignKey('Teacher')

    def __unicode__(self):
        return self.number


class Language(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title


class Teacher(User):
    middleName = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, choices=POSITIONS)
    department = models.ForeignKey(Department)

    class Meta:
        verbose_name = 'Teacher'

    def __unicode__(self):
        return self.first_name + ' ' +  self.last_login


class Benefits(models.Model):
    type = models.CharField(max_length=255)

    def __unicode__(self):
        return self.type


class Student(User):
    middleName = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    language = models.ForeignKey(Language)
    phone = models.CharField(max_length=30)
    benefits = models.ManyToManyField(Benefits)
    isProcurement = models.BooleanField(default=False)
    group = models.ForeignKey(Group)
    dateBirth = models.DateField()
    nationality = models.CharField(max_length=50)
    maritalStatus = models.CharField(max_length=50, choices=MARITAL_STATUSES)
    sex = models.CharField(max_length=50, choices=SEX)
    school = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Student'

    def __unicode__(self):
        return self.first_name + ' ' +  self.last_login


class Parents(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    position = models.CharField(max_length=255)
    student = models.ForeignKey(Student)

    def __unicode__(self):
        return self.fullname

class Subject(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=SUBJECT_TYPES)

    def __unicode__(self):
        return self.title

class Additional(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    student = models.ForeignKey(Student)

    def __unicode__(self):
        return self.title

    def __unicode__(self):
        return self.group

class ClassRoom(models.Model):
    number = models.CharField(max_length=50)

    def __unicode__(self):
        return self.number

class Class(models.Model):
    subject = models.ForeignKey(Subject)
    teacher = models.ForeignKey(Teacher)
    classRoom = models.ForeignKey(ClassRoom)
    day = models.CharField(max_length=20, choices=DAYS)
    number_of_week = models.CharField(max_length=2, choices=(('1', 1), ('2', 2)))
    number = models.IntegerField()

    def __unicode__(self):
        return self.subject

class Event(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

class StudentWork(models.Model):
    text = models.TextField()
    year = models.CharField(max_length=10)
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.text

class PublicPlan(models.Model):
    event = models.ForeignKey(Event)
    date = models.DateTimeField()
    responsive = models.ForeignKey(Teacher)
    description = models.CharField(max_length=255, blank=True)
    amount_hours = models.FloatField()
    amount_present = models.IntegerField()

    def __unicode__(self):
        return self.description

class Report(models.Model):
    date = models.DateField()
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return self.event

class Pass(models.Model):
    student = models.ForeignKey(Student)
    date = models.DateField()
    type = models.CharField(max_length=50, choices=PASS_TYPES)
    class_passed = models.ForeignKey(Class)

    def __unicode__(self):
        return ' '.join([self.student.first_name, self.student.last_name, self.type, self.date])

#models views
class PassView(admin.ModelAdmin):
    list_display = ('student', 'date', 'type', 'class_passed')

class AdditionalAdminView(admin.ModelAdmin):
    list_display = ('title',)

class BenefitsAdminView(admin.ModelAdmin):
    list_display = ('type',)

class ClassRoomAdminView(admin.ModelAdmin):
    list_display = ('number',)

class ClassAdminView(admin.ModelAdmin):
    list_display = ('subject',)

class DepartmentAdminView(admin.ModelAdmin):
    list_display = ('title',)

class EventAdminView(admin.ModelAdmin):
    list_display = ('title',)

class FacultyAdminView(admin.ModelAdmin):
    list_display = ('title',)

class GroupAdminView(admin.ModelAdmin):
    list_display = ('number',)

class LanguageAdminView(admin.ModelAdmin):
    list_display = ('title',)

class ParentsAdminView(admin.ModelAdmin):
    list_display = ('fullname',)

class PublicPlanAdminView(admin.ModelAdmin):
    list_display = ('description',)

class ReportAdminView(admin.ModelAdmin):
    list_display = ('date',)

class StudentAdminView(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

class StudentWorkAdminView(admin.ModelAdmin):
    list_display = ('text',)

class SubjectAdminView(admin.ModelAdmin):
    list_display = ('title',)

class TeacherAdminView(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')

#register
try:
    admin.site.register(Additional, AdditionalAdminView)
    admin.site.register(Benefits, BenefitsAdminView)
    admin.site.register(ClassRoom, ClassRoomAdminView)
    admin.site.register(Class, ClassAdminView)
    admin.site.register(Department, DepartmentAdminView)
    admin.site.register(Event, EventAdminView)
    admin.site.register(Faculty, FacultyAdminView)
    admin.site.register(Group, GroupAdminView)
    admin.site.register(Language, LanguageAdminView)
    admin.site.register(Parents, ParentsAdminView)
    admin.site.register(PublicPlan, PublicPlanAdminView)
    admin.site.register(Report, ReportAdminView)
    admin.site.register(Student, StudentAdminView)
    admin.site.register(StudentWork, StudentWorkAdminView)
    admin.site.register(Subject, SubjectAdminView)
    admin.site.register(Teacher, TeacherAdminView)
except Exception:
    pass