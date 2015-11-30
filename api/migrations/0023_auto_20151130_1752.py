# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20151130_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='plotItem',
            new_name='plot_item',
        ),
        migrations.AddField(
            model_name='noveltoken',
            name='character',
            field=models.ForeignKey(null=True, to='api.Character', blank=True),
        ),
        migrations.AddField(
            model_name='noveltoken',
            name='place',
            field=models.ForeignKey(null=True, to='api.Place', blank=True),
        ),
        migrations.AddField(
            model_name='noveltoken',
            name='plot_item',
            field=models.ForeignKey(null=True, to='api.PlotItem', blank=True),
        ),
        migrations.AlterField(
            model_name='noveltoken',
            name='token',
            field=models.ForeignKey(null=True, to='api.Token', blank=True),
        ),
    ]
