# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20150207_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='bedrooms',
            field=models.PositiveSmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicant',
            name='income',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='applicant',
            name='name',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
    ]
