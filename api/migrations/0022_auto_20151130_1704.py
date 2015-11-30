# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20151126_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vote',
            options={},
        ),
        migrations.AddField(
            model_name='vote',
            name='character',
            field=models.ForeignKey(null=True, to='api.Character', blank=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='place',
            field=models.ForeignKey(null=True, to='api.Place', blank=True),
        ),
        migrations.AddField(
            model_name='vote',
            name='plotItem',
            field=models.ForeignKey(null=True, to='api.PlotItem', blank=True),
        ),
        migrations.AlterField(
            model_name='vote',
            name='token',
            field=models.ForeignKey(null=True, to='api.Token', blank=True),
        ),
        migrations.AlterOrderWithRespectTo(
            name='vote',
            order_with_respect_to='chapter',
        ),
    ]
