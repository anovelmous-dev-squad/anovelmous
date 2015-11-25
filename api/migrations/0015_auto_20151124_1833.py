# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20151124_1616'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noveltoken',
            options={'ordering': ('ordinal',)},
        ),
        migrations.AddField(
            model_name='chapter',
            name='ordinal',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
