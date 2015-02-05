# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150127_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='is_completed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='novel',
            name='is_completed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='token',
            name='is_valid',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
