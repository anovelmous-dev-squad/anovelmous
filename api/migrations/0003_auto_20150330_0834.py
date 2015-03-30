# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150304_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='voting_duration',
            field=models.PositiveSmallIntegerField(default=15),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='novel',
            name='voting_duration',
            field=models.PositiveSmallIntegerField(default=15),
            preserve_default=True,
        ),
    ]
