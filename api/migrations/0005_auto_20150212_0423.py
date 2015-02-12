# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20150205_0119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formattednoveltoken',
            options={'ordering': ['ordinal']},
        ),
        migrations.AlterModelOptions(
            name='noveltoken',
            options={'ordering': ['ordinal']},
        ),
        migrations.AlterModelOptions(
            name='vote',
            options={'ordering': ['ordinal']},
        ),
        migrations.AlterUniqueTogether(
            name='formattednoveltoken',
            unique_together=set([('ordinal', 'chapter')]),
        ),
        migrations.AlterUniqueTogether(
            name='noveltoken',
            unique_together=set([('ordinal', 'chapter')]),
        ),
    ]
