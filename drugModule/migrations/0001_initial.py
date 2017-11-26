# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='DrugName', max_length=100)),
                ('description', models.CharField(verbose_name='DrugDescription', max_length=500, blank=True, null=True)),
                ('toxicity', models.CharField(verbose_name='Toxicity', max_length=200, blank=True, null=True)),
                ('interaction', models.ForeignKey(blank=True, null=True, related_name='sides', related_query_name='sides', to='drugModule.Drug')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
