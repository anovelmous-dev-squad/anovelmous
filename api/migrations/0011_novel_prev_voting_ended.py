# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20151123_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='prev_voting_ended',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 24, 3, 32, 32, 812198, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
