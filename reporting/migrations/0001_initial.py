# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subject', models.CharField(max_length=25)),
                ('classroom', models.CharField(max_length=25)),
                ('day', models.CharField(max_length=20, choices=[('Monday', 'Понеділок'), ('Tuesday', 'Вівторок'), ('Wednesday', 'Середа'), ('Thursday', 'Четвер'), ('Friday', "П'ятниця"), ('Saturday', 'Субота'), ('Sunday', 'Неділя')])),
                ('numberOfWeek', models.CharField(max_length=2, choices=[('1', 1), ('2', 2)])),
                ('number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255, blank=True, null=True)),
                ('startFirstSemester', models.DateField(blank=True, null=True)),
                ('startSecondSemester', models.DateField(blank=True, null=True)),
                ('endFirstSemester', models.DateField(blank=True, null=True)),
                ('endSecondSemester', models.DateField(blank=True, null=True)),
                ('amountOfWeekInFirstSemester', models.IntegerField(blank=True, null=True)),
                ('amountOfWeekInSecondSemester', models.IntegerField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('number', models.CharField(max_length=25)),
                ('yearStudy', models.IntegerField()),
                ('tuition', models.CharField(max_length=50, choices=[('stationary', 'Стаціонар'), ('extramural', 'Заочна форма')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('fullName', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=50, choices=[('pass', 'Без поважної причини'), ('sickness', 'По хворобі'), ('statement', 'Заява'), ('watch', 'Чергування')])),
                ('class_passed', models.ForeignKey(to='reporting.Class', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('event', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=100)),
                ('responsive', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, blank=True, null=True)),
                ('amount_hours', models.FloatField(blank=True, null=True)),
                ('amount_present', models.IntegerField(blank=True, null=True)),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('group', models.ForeignKey(to='reporting.Group', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('firstName', models.CharField(max_length=255, blank=True)),
                ('lastName', models.CharField(max_length=255, blank=True)),
                ('middleName', models.CharField(max_length=255, blank=True)),
                ('email', models.EmailField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('currentAddress', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('isProcurement', models.BooleanField(default=False)),
                ('dateBirth', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
                ('maritalStatus', models.CharField(max_length=50, choices=[('single', 'Не одружений'), ('married', 'Одружений')])),
                ('sex', models.CharField(max_length=50, choices=[('male', 'Чоловіча'), ('female', 'Жіноча')])),
                ('school', models.CharField(max_length=255)),
                ('additional', models.CharField(max_length=255, blank=True, null=True)),
                ('benefits', models.ManyToManyField(to='reporting.Benefits', blank=True, null=True)),
                ('father', models.ForeignKey(related_name='father', to='reporting.Parents', blank=True, null=True)),
                ('group', models.ForeignKey(to='reporting.Group', blank=True, null=True)),
                ('language', models.ForeignKey(to='reporting.Language', null=True)),
                ('mother', models.ForeignKey(related_name='mother', to='reporting.Parents', blank=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True, null=True)),
            ],
            options={
                'verbose_name': 'Student',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField()),
                ('year', models.CharField(max_length=10)),
                ('group', models.ForeignKey(to='reporting.Group', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('firstName', models.CharField(max_length=255, blank=True)),
                ('lastName', models.CharField(max_length=255, blank=True)),
                ('middleName', models.CharField(max_length=255, blank=True)),
                ('position', models.CharField(max_length=255, choices=[('dean', 'Декан'), ('Head of Department', 'Завідувач кафедри'), ('Deputy Dean', 'Заступник декана'), ('teacher', 'Викладач')])),
                ('department', models.ForeignKey(to='reporting.Department', blank=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True, null=True)),
            ],
            options={
                'verbose_name': 'Teacher',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pass',
            name='student',
            field=models.ForeignKey(to='reporting.Student', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='culturalWork',
            field=models.ForeignKey(related_name='cultural', to='reporting.Student', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='curator',
            field=models.ForeignKey(to='reporting.Teacher', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='department',
            field=models.ForeignKey(to='reporting.Department', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='deputyHeadman',
            field=models.ForeignKey(related_name='deputy', to='reporting.Student', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='editorialBoard',
            field=models.ManyToManyField(related_name='editorial', to='reporting.Student', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='healthWork',
            field=models.ForeignKey(related_name='health', to='reporting.Student', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.ForeignKey(related_name='leader', to='reporting.Student', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='organizer',
            field=models.ForeignKey(related_name='organiser', to='reporting.Student', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='otherTasks',
            field=models.ManyToManyField(related_name='other', to='reporting.Student', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='faculty',
            name='dean',
            field=models.ForeignKey(to='reporting.Teacher', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(to='reporting.Faculty', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='department',
            name='headOfDepartment',
            field=models.ForeignKey(related_name='head', to='reporting.Teacher', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='group',
            field=models.ForeignKey(to='reporting.Group', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(to='reporting.Teacher', blank=True, null=True),
            preserve_default=True,
        ),
    ]
