# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_populate_uuid_values_20150630_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='client_id',
            field=models.UUIDField(unique=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='formattednoveltoken',
            name='client_id',
            field=models.UUIDField(unique=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='novel',
            name='client_id',
            field=models.UUIDField(unique=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='noveltoken',
            name='client_id',
            field=models.UUIDField(unique=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='token',
            name='client_id',
            field=models.UUIDField(unique=True, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='vote',
            name='client_id',
            field=models.UUIDField(unique=True, default=uuid.uuid4),
        ),
    ]
