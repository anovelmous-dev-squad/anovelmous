# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20151130_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactervote',
            name='character',
            field=models.ForeignKey(to='api.Character', related_name='votes'),
        ),
        migrations.AlterField(
            model_name='placevote',
            name='place',
            field=models.ForeignKey(to='api.Place', related_name='votes'),
        ),
        migrations.AlterField(
            model_name='plotitemvote',
            name='plot_item',
            field=models.ForeignKey(to='api.PlotItem', related_name='votes'),
        ),
        migrations.AlterField(
            model_name='plotvote',
            name='plot',
            field=models.ForeignKey(to='api.Plot', related_name='votes'),
        ),
    ]
