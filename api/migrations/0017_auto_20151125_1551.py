# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20151125_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel',
            name='stage',
            field=models.ForeignKey(to='api.Stage', default=1),
        ),
    ]
