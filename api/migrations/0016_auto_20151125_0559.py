# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20151124_1833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ('ordinal',)},
        ),
        migrations.AlterField(
            model_name='novel',
            name='prev_voting_ended',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
