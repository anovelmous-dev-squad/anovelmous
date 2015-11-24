# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_stage_ordinal'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='novel',
            field=models.ForeignKey(to='api.Novel', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='novel',
            field=models.ForeignKey(to='api.Novel', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plot',
            name='novel',
            field=models.ForeignKey(to='api.Novel', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plotitem',
            name='novel',
            field=models.ForeignKey(to='api.Novel', default=1),
            preserve_default=False,
        ),
    ]
