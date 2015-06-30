# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150330_0834'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='client_id',
            field=models.UUIDField(null=True, default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='formattednoveltoken',
            name='client_id',
            field=models.UUIDField(null=True, default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='novel',
            name='client_id',
            field=models.UUIDField(null=True, default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='noveltoken',
            name='client_id',
            field=models.UUIDField(null=True, default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='token',
            name='client_id',
            field=models.UUIDField(null=True, default=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='vote',
            name='client_id',
            field=models.UUIDField(null=True, default=uuid.uuid4),
        ),
    ]
