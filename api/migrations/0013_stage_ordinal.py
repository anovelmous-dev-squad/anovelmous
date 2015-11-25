# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_novel_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='ordinal',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
