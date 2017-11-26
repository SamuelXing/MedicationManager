# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserModule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normaluser',
            name='created_at',
            field=models.DateTimeField(verbose_name='joined at', auto_now_add=True),
        ),
    ]
