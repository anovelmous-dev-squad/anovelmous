# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20151126_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='novel',
            old_name='selected_plot',
            new_name='plot',
        ),
    ]
