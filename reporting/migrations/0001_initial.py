# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('day', models.CharField(max_length=20, choices=[('monday', 'Понеділок'), ('tuesday', 'Вівторок'), ('wednesday', 'Середа'), ('Thursday', 'Четвер'), ('Friday', "П'ятниця"), ('Saturday', 'Субота'), ('Sunday', 'Неділя')])),
                ('number_of_week', models.CharField(max_length=2, choices=[('1', 1), ('2', 2)])),
                ('number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('number', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PublicPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateTimeField()),
                ('description', models.CharField(max_length=255, blank=True)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField()),
                ('event', models.ForeignKey(to='reporting.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('group', models.ForeignKey(to='reporting.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('middleName', models.CharField(max_length=255, blank=True)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=30)),
                ('isProcurement', models.BooleanField(default=False)),
                ('dateBirth', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
                ('maritalStatus', models.CharField(max_length=50, choices=[('single', 'Не одружений'), ('married', 'Одружений')])),
                ('sex', models.CharField(max_length=50, choices=[('male', 'Чоловіча'), ('female', 'Жіноча')])),
                ('school', models.CharField(max_length=255)),
                ('benefits', models.ManyToManyField(to='reporting.Benefits')),
                ('group', models.ForeignKey(to='reporting.Group')),
                ('language', models.ForeignKey(to='reporting.Language')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='StudentWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=50, choices=[('lection', 'Лекція'), ('practic', 'Практика'), ('lab', 'Лабораторний практикум')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, parent_link=True, to=settings.AUTH_USER_MODEL)),
                ('middleName', models.CharField(max_length=255, blank=True)),
                ('position', models.CharField(max_length=255, choices=[('dean', 'Декан'), ('Head of Department', 'Завідувач кафедри'), ('teacher', 'Викладач')])),
                ('department', models.ForeignKey(to='reporting.Department')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='publicplan',
            name='responsive',
            field=models.ForeignKey(to='reporting.Teacher'),
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
            field=models.ForeignKey(to='reporting.Teacher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='department',
            field=models.ForeignKey(to='reporting.Department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.ForeignKey(to='reporting.Student', related_name='gr_lead'),
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
            name='schedule',
            field=models.ForeignKey(to='reporting.Schedule'),
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
