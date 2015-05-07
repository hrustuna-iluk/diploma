#-*-coding:UTF-8-*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import datetime

POSITIONS = (
    ('dean', 'Декан'),
    ('Head of Department', 'Завідувач кафедри'),
    ('Deputy Dean', 'Заступник декана'),
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
    ('lecture', 'Лекція'),
    ('practice', 'Практика')
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
    title = models.CharField(max_length=255, blank=True, null=True)
    startFirstSemester = models.DateField(null=True, blank=True)
    startSecondSemester = models.DateField(null=True, blank=True)
    endFirstSemester = models.DateField(null=True, blank=True)
    endSecondSemester = models.DateField(null=True, blank=True)
    amountOfWeekInFirstSemester = models.IntegerField(null=True, blank=True)
    amountOfWeekInSecondSemester = models.IntegerField(null=True, blank=True)
    dean = models.ForeignKey('Teacher', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            startWeekFirst = datetime.date(
                self.startFirstSemester.year,
                self.startFirstSemester.month,
                self.startFirstSemester.day
                ).isocalendar()[1]
            endWeekFirst = datetime.date(
                self.endFirstSemester.year,
                self.endFirstSemester.month,
                self.endFirstSemester.day
            ).isocalendar()[1]
            startWeekSecond = datetime.date(
                self.startSecondSemester.year,
                self.startSecondSemester.month,
                self.startSecondSemester.day
            ).isocalendar()[1]
            endWeekSecond = datetime.date(
                self.endSecondSemester.year,
                self.endSecondSemester.month,
                self.endSecondSemester.day
            ).isocalendar()[1]

            self.amountOfWeekInFirstSemester = endWeekFirst - startWeekFirst
            self.amountOfWeekInSecondSemester = endWeekSecond - startWeekSecond
        except AttributeError:
            pass
        super(Faculty, self).save(*args, **kwargs)


class Department(models.Model):
    title = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    headOfDepartment = models.ForeignKey('Teacher', null=True, related_name='head', blank=True)
    faculty = models.ForeignKey(Faculty, null=True, blank=True)

    def __str__(self):
        return self.title


class Group(models.Model):
    number = models.CharField(max_length=25)
    short_form = models.BooleanField(default=False)
    master = models.BooleanField(default=False)
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
    user = models.ForeignKey(User, unique=True, null=True, blank=True)
    firstName = models.CharField(max_length=255, blank=True)
    lastName = models.CharField(max_length=255, blank=True)
    middleName = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255)
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

    class Meta:
        verbose_name_plural = 'Benefits'


class Student(models.Model):
    user = models.ForeignKey(User, unique=True, null=True, blank=True)
    firstName = models.CharField(max_length=255, blank=True)
    lastName = models.CharField(max_length=255, blank=True)
    middleName = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255)
    father = models.ForeignKey('Parents', null=True, blank=True, related_name='father')
    mother = models.ForeignKey('Parents', null=True, blank=True, related_name='mother')
    address = models.CharField(max_length=255)
    currentAddress = models.CharField(max_length=255)
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
    additional = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Student'

    def __str__(self):
        return self.firstName + ' ' + self.lastName

    def full_name(self):
        return self.lastName + ' ' + self.firstName + ' ' + self.middleName


class Parents(models.Model):
    fullName = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.fullName

    class Meta:
        verbose_name_plural = 'Parents'


class Class(models.Model):
    subject = models.CharField(max_length=25)
    type = models.CharField(max_length=50, choices=SUBJECT_TYPES)
    teacher = models.ForeignKey(Teacher, null=True, blank=True)
    classroom = models.CharField(max_length=25)
    day = models.CharField(max_length=20, choices=DAYS)
    numberOfWeek = models.CharField(max_length=2, choices=(('1', 1), ('2', 2)))
    number = models.IntegerField()
    semester = models.CharField(max_length=2, choices=(('1', 1), ('2', 2)))
    group = models.ForeignKey('Group', null=True, blank=True)

    def __str__(self):
        return self.subject + ' ' + self.classroom

    class Meta:
        verbose_name_plural = 'Classes'


class StudentWork(models.Model):
    text = models.TextField()
    year = models.CharField(max_length=10)
    group = models.ForeignKey(Group, null=True, blank=True)

    def __str__(self):
        return self.text


class PublicPlan(models.Model):
    event = models.CharField(max_length=255)
    date = models.CharField(max_length=100)
    responsive = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    amount_hours = models.FloatField(null=True, blank=True)
    amount_present = models.IntegerField(null=True, blank=True)
    semester = models.IntegerField(null=True, blank=True)
    group = models.ForeignKey(Group, null=True, blank=True)

    def __str__(self):
        return self.description


class Pass(models.Model):
    student = models.ForeignKey(Student, null=True, blank=True)
    date = models.DateField()
    type = models.CharField(max_length=50, choices=PASS_TYPES)
    class_passed = models.ForeignKey(Class, null=True, blank=True)

    def __str__(self):
        return ' '.join([self.student.firstName, self.student.lastName, self.type, self.class_passed.subject])

    def __str(self):
        return str(self.id) + ' ' + str(self.group.number)

    class Meta:
        verbose_name_plural = 'Passes'
        unique_together = ('student', 'date', 'class_passed')


#models views
class PassView(admin.ModelAdmin):
    list_display = ('student', 'date', 'type', 'class_passed')


class BenefitsAdminView(admin.ModelAdmin):
    list_display = ('type',)


class ClassAdminView(admin.ModelAdmin):
    list_display = ('subject',)


class DepartmentAdminView(admin.ModelAdmin):
    list_display = ('title',)


class FacultyAdminView(admin.ModelAdmin):
    list_display = ('title',)


class GroupAdminView(admin.ModelAdmin):
    list_display = ('number',)


class LanguageAdminView(admin.ModelAdmin):
    list_display = ('title',)


class ParentsAdminView(admin.ModelAdmin):
    list_display = ('fullName',)


class PublicPlanAdminView(admin.ModelAdmin):
    list_display = ('description',)


class StudentAdminView(admin.ModelAdmin):
    list_display = ('firstName', 'lastName')


class StudentWorkAdminView(admin.ModelAdmin):
    list_display = ('text',)


class TeacherAdminView(admin.ModelAdmin):
    list_display = ('firstName', 'lastName')

#register
try:
    admin.site.register(Benefits, BenefitsAdminView)
    admin.site.register(Class, ClassAdminView)
    admin.site.register(Department, DepartmentAdminView)
    admin.site.register(Faculty, FacultyAdminView)
    admin.site.register(Group, GroupAdminView)
    admin.site.register(Language, LanguageAdminView)
    admin.site.register(Parents, ParentsAdminView)
    admin.site.register(PublicPlan, PublicPlanAdminView)
    admin.site.register(Student, StudentAdminView)
    admin.site.register(StudentWork, StudentWorkAdminView)
    admin.site.register(Teacher, TeacherAdminView)
    admin.site.register(Pass, PassView)
except Exception:
    pass