#-*-coding:UTF-8-*-
from django.db import models
from django.contrib import admin

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
    ('1', 'Лекція'),
    ('2', 'Практика')
)

TUITION_TYPES = (
    ('stationary', 'Стаціонар'),
    ('extramural', 'Заочна форма'),
)

DAYS = (
    ('Monday', 'Понеділок'),
    ('Tuesday', 'Вівторок'),
    ('Wednesday', 'Середа'),
    ('Thursday', 'Четвер'),
    ('Friday', "П'ятниця"),
    ('Saturday', 'Субота'),
    ('Sunday', 'Неділя')
)

PASS_TYPES = (
    ('pass', "Без поважної причини"),
    ('sickness', "По хворобі"),
    ('statement', "Заява"),
    ('watch', "Чергування"),
)


class Faculty(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Department(models.Model):
    title = models.CharField(max_length=255)
    headOfDepartment = models.ForeignKey('Teacher', null=True, related_name='head', blank=True)

    def __str__(self):
        return self.title


class Group(models.Model):
    number = models.CharField(max_length=25)
    department = models.ForeignKey(Department, null=True, blank=True)
    leader = models.ForeignKey('Student', null=True, related_name='leader', blank=True)
    deputyHeadman = models.ForeignKey('Student', null=True, related_name='deputy', blank=True)
    organizer = models.ForeignKey('Student', null=True, related_name='organiser', blank=True)
    culturalWork = models.ForeignKey('Student', null=True, related_name='cultural', blank=True)
    healthWork = models.ForeignKey('Student', null=True, related_name='health', blank=True)
    editorialBoard = models.ManyToManyField('Student', null=True, related_name='editorial', blank=True)
    otherTasks = models.ManyToManyField('Student', null=True, related_name='other', blank=True)
    yearStudy = models.IntegerField()
    tuition = models.CharField(max_length=50, choices=TUITION_TYPES)
    curator = models.ForeignKey('Teacher', blank=True, null=True)

    def __str__(self):
        return self.number


class Language(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    firstName = models.CharField(max_length=255, blank=True)
    lastName = models.CharField(max_length=255, blank=True)
    middleName = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, choices=POSITIONS)
    department = models.ForeignKey(Department, null=True, blank=True)

    class Meta:
        verbose_name = 'Teacher'

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Benefits(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Student(models.Model):
    firstName = models.CharField(max_length=255, blank=True)
    lastName = models.CharField(max_length=255, blank=True)
    middleName = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    language = models.ForeignKey(Language, null=True)
    phone = models.CharField(max_length=30)
    benefits = models.ManyToManyField(Benefits, blank=True, null=True)
    isProcurement = models.BooleanField(default=False)
    group = models.ForeignKey(Group, null=True, blank=True)
    dateBirth = models.DateField()
    nationality = models.CharField(max_length=50)
    maritalStatus = models.CharField(max_length=50, choices=MARITAL_STATUSES)
    sex = models.CharField(max_length=50, choices=SEX)
    school = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Student'

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Parents(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    position = models.CharField(max_length=255)
    student = models.ForeignKey(Student, null=True, blank=True)

    def __str__(self):
        return self.fullname


class Additional(models.Model):
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    student = models.ForeignKey(Student, null=True, blank=True)

    def __str__(self):
        return self.title + ' ' + self.student.firstName + ' ' + self.student.lastName


class Class(models.Model):
    subject = models.CharField(max_length=25)
    teacher = models.ForeignKey(Teacher, null=True, blank=True)
    classRoom = models.CharField(max_length=25)
    day = models.CharField(max_length=20, choices=DAYS)
    number_of_week = models.CharField(max_length=2, choices=(('1', 1), ('2', 2)))
    number = models.IntegerField()
    group = models.ForeignKey('Group', null=True, blank=True)

    def __str__(self):
        return self.subject + ' ' + self.classRoom


class Event(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class StudentWork(models.Model):
    text = models.TextField()
    year = models.CharField(max_length=10)
    group = models.ForeignKey(Group, null=True, blank=True)

    def __str__(self):
        return self.text


class PublicPlan(models.Model):
    event = models.ForeignKey(Event, null=True, blank=True)
    date = models.DateTimeField()
    responsive = models.ForeignKey(Teacher, null=True, blank=True)
    description = models.CharField(max_length=255, blank=True)
    amount_hours = models.FloatField()
    amount_present = models.IntegerField()

    def __str__(self):
        return self.description


class Report(models.Model):
    date = models.DateField()
    event = models.ForeignKey(Event, null=True, blank=True)

    def __str__(self):
        return self.event.title


class Pass(models.Model):
    student = models.ForeignKey(Student, null=True, blank=True)
    date = models.DateField()
    type = models.CharField(max_length=50, choices=PASS_TYPES)
    class_passed = models.ForeignKey(Class, null=True, blank=True)

    def __str__(self):
        return ' '.join([self.student.first_name, self.student.last_name, self.type, self.date])

    def __str(self):
        return str(self.id) + ' ' + str(self.group.number)


#models views
class PassView(admin.ModelAdmin):
    list_display = ('student', 'date', 'type', 'class_passed')


class AdditionalAdminView(admin.ModelAdmin):
    list_display = ('title',)


class BenefitsAdminView(admin.ModelAdmin):
    list_display = ('type',)


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
    list_display = ('firstName', 'lastName')


class StudentWorkAdminView(admin.ModelAdmin):
    list_display = ('text',)


class TeacherAdminView(admin.ModelAdmin):
    list_display = ('firstName', 'lastName')

#register
try:
    admin.site.register(Additional, AdditionalAdminView)
    admin.site.register(Benefits, BenefitsAdminView)
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
    admin.site.register(Teacher, TeacherAdminView)
except Exception:
    pass