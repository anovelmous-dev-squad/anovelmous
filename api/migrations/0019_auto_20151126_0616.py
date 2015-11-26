# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20151126_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='characters',
            field=models.ManyToManyField(related_name='featured_novels_character', to='api.Character', blank=True),
        ),
        migrations.AddField(
            model_name='novel',
            name='places',
            field=models.ManyToManyField(related_name='featured_novels_place', to='api.Place', blank=True),
        ),
        migrations.AddField(
            model_name='novel',
            name='plot_items',
            field=models.ManyToManyField(related_name='featured_novels_plot_item', to='api.PlotItem', blank=True),
        ),
        migrations.AddField(
            model_name='novel',
            name='selected_plot',
            field=models.ForeignKey(related_name='featured_novels_plot', null=True, to='api.Plot', blank=True),
        ),
    ]
