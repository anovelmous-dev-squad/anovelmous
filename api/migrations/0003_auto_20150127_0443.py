# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150124_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='novel',
            field=models.ForeignKey(related_name='chapters', to='api.Novel'),
            preserve_default=True,
        ),
    ]
