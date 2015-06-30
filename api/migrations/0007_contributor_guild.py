# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import uuid
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('api', '0006_remove_uuid_null_20150630_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, auto_created=True, parent_link=True, serialize=False)),
                ('client_id', models.UUIDField(unique=True, default=uuid.uuid4)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('group_ptr', models.OneToOneField(primary_key=True, to='auth.Group', auto_created=True, parent_link=True, serialize=False)),
                ('client_id', models.UUIDField(unique=True, default=uuid.uuid4)),
            ],
            bases=('auth.group',),
        ),
    ]
