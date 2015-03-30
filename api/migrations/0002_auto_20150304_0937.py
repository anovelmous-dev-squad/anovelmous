# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formattednoveltoken',
            options={},
        ),
        migrations.AlterModelOptions(
            name='noveltoken',
            options={},
        ),
        migrations.AlterField(
            model_name='formattednoveltoken',
            name='chapter',
            field=models.ForeignKey(to='api.Chapter', related_name='formatted_novel_tokens'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noveltoken',
            name='chapter',
            field=models.ForeignKey(to='api.Chapter', related_name='novel_tokens'),
            preserve_default=True,
        ),
    ]
