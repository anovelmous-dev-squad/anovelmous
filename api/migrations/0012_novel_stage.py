# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_novel_prev_voting_ended'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='stage',
            field=models.ForeignKey(default=1, to='api.Stage'),
            preserve_default=False,
        ),
    ]
