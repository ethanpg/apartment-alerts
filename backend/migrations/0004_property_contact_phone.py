# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20150207_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='contact_phone',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
