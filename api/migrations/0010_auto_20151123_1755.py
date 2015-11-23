# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_character_place_plot_plotitem_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='contributor',
            field=models.ForeignKey(related_name='characters', default=1, to='api.Contributor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='contributor',
            field=models.ForeignKey(related_name='places', default=1, to='api.Contributor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plot',
            name='contributor',
            field=models.ForeignKey(related_name='plots', default=1, to='api.Contributor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plotitem',
            name='contributor',
            field=models.ForeignKey(related_name='plot_items', default=1, to='api.Contributor'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='noveltoken',
            name='chapter',
            field=models.ForeignKey(related_name='tokens', to='api.Chapter'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='contributor',
            field=models.ForeignKey(related_name='votes', to='api.Contributor'),
        ),
    ]
