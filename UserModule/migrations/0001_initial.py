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
            name='NormalUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nickname', models.CharField(verbose_name='username', max_length=50)),
                ('created_at', models.DateTimeField(verbose_name='join at', auto_now_add=True)),
                ('user', models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Information',
                'verbose_name_plural': 'User Information',
                'ordering': ['-created_at'],
            },
        ),
    ]
