# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Additional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('day', models.CharField(choices=[('monday', 'Понеділок'), ('tuesday', 'Вівторок'), ('wednesday', 'Середа'), ('Thursday', 'Четвер'), ('Friday', "П'ятниця"), ('Saturday', 'Субота'), ('Sunday', 'Неділя')], max_length=20)),
                ('number_of_week', models.CharField(choices=[('1', 1), ('2', 2)], max_length=2)),
                ('number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('number', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('number', models.CharField(max_length=25)),
                ('leader', models.CharField(max_length=255)),
                ('yearStudy', models.IntegerField()),
                ('tuition', models.CharField(choices=[('stationary', 'Стаціонар'), ('extramural', 'Заочна форма')], max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('fullname', models.CharField(max_length=255)),
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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('pass', 'Без поважної причини'), ('sickness', 'По хворобі'), ('statement', "За'ява"), ('watch', 'Чергування')], max_length=50)),
                ('class_passed', models.ForeignKey(to='reporting.Class')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicPlan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateTimeField()),
                ('description', models.CharField(blank=True, max_length=255)),
                ('amount_hours', models.FloatField()),
                ('amount_present', models.IntegerField()),
                ('event', models.ForeignKey(to='reporting.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('event', models.ForeignKey(to='reporting.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('firstName', models.CharField(blank=True, max_length=255)),
                ('lastName', models.CharField(blank=True, max_length=255)),
                ('middleName', models.CharField(blank=True, max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('isProcurement', models.BooleanField(default=False)),
                ('dateBirth', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
                ('maritalStatus', models.CharField(choices=[('single', 'Не одружений'), ('married', 'Одружений')], max_length=50)),
                ('sex', models.CharField(choices=[('male', 'Чоловіча'), ('female', 'Жіноча')], max_length=50)),
                ('school', models.CharField(max_length=255)),
                ('benefits', models.ManyToManyField(to='reporting.Benefits', null=True, blank=True)),
                ('group', models.ForeignKey(to='reporting.Group')),
                ('language', models.ForeignKey(to='reporting.Language')),
            ],
            options={
                'verbose_name': 'Student',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.TextField()),
                ('year', models.CharField(max_length=10)),
                ('group', models.ForeignKey(to='reporting.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('lection', 'Лекція'), ('practic', 'Практика'), ('lab', 'Лабораторний практикум')], max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('firstName', models.CharField(blank=True, max_length=255)),
                ('lastName', models.CharField(blank=True, max_length=255)),
                ('middleName', models.CharField(blank=True, max_length=255)),
                ('position', models.CharField(choices=[('dean', 'Декан'), ('Head of Department', 'Завідувач кафедри'), ('teacher', 'Викладач')], max_length=255)),
                ('department', models.ForeignKey(to='reporting.Department')),
            ],
            options={
                'verbose_name': 'Teacher',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='publicplan',
            name='responsive',
            field=models.ForeignKey(to='reporting.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pass',
            name='student',
            field=models.ForeignKey(to='reporting.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='parents',
            name='student',
            field=models.ForeignKey(to='reporting.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='curator',
            field=models.ForeignKey(to='reporting.Teacher', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='department',
            field=models.ForeignKey(to='reporting.Department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='classRoom',
            field=models.ForeignKey(to='reporting.ClassRoom'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='subject',
            field=models.ForeignKey(to='reporting.Subject'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='class',
            name='teacher',
            field=models.ForeignKey(to='reporting.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='additional',
            name='student',
            field=models.ForeignKey(to='reporting.Student'),
            preserve_default=True,
        ),
    ]
