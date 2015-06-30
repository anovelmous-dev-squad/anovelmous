# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import time


def gen_uuid(apps, schema_editor):
    model_names = ['novel', 'chapter', 'token', 'noveltoken', 'formattednoveltoken', 'vote']
    for model_name in model_names:
        model = apps.get_model('api', model_name)
        for row in model.objects.all():
            row.client_id = uuid.uuid4()
            row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_add_uuid_field_20150630_0255'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
