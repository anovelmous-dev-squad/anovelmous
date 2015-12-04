# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20151201_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charactervote',
            name='contributor',
            field=models.ForeignKey(related_name='charactervotes', to='api.Contributor'),
        ),
        migrations.AlterField(
            model_name='placevote',
            name='contributor',
            field=models.ForeignKey(related_name='placevotes', to='api.Contributor'),
        ),
        migrations.AlterField(
            model_name='plotitemvote',
            name='contributor',
            field=models.ForeignKey(related_name='plotitemvotes', to='api.Contributor'),
        ),
        migrations.AlterField(
            model_name='plotvote',
            name='contributor',
            field=models.ForeignKey(related_name='plotvotes', to='api.Contributor'),
        ),
    ]
