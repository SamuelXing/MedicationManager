# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('drugModule', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('frequencies', models.CharField(max_length=15, default='TwoTimes', choices=[('OneTime', 'OneTimePerDay'), ('TwoTimes', 'TwoTimesPerDay'), ('ThreeTimes', 'ThreeTimesPerDay')])),
                ('dose', models.CharField(max_length=5, default='Three', choices=[('One', 'OnePillPerTime'), ('Two', 'TwoPillsPerTime'), ('Three', 'TwoPillsPerTime')])),
                ('startDate', models.DateTimeField(auto_now_add=True)),
                ('endDate', models.DateTimeField()),
                ('drug', models.ForeignKey(to='drugModule.Drug')),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
