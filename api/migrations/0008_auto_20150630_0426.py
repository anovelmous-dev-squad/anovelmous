# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_contributor_guild'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='user',
        ),
        migrations.AddField(
            model_name='vote',
            name='contributor',
            field=models.ForeignKey(to='api.Contributor', default=1),
            preserve_default=False,
        ),
    ]
