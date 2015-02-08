# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='phone_number',
            field=models.CharField(unique=True, max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='applicants',
            field=models.ManyToManyField(to='backend.Applicant', blank=True),
            preserve_default=True,
        ),
    ]
