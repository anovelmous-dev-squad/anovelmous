# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20151126_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='novel',
            field=models.ForeignKey(related_name='proposed_characters', to='api.Novel'),
        ),
        migrations.AlterField(
            model_name='place',
            name='novel',
            field=models.ForeignKey(related_name='proposed_places', to='api.Novel'),
        ),
        migrations.AlterField(
            model_name='plot',
            name='novel',
            field=models.ForeignKey(related_name='proposed_plots', to='api.Novel'),
        ),
        migrations.AlterField(
            model_name='plotitem',
            name='novel',
            field=models.ForeignKey(related_name='proposed_plotitems', to='api.Novel'),
        ),
    ]
