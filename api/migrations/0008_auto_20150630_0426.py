# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


def migrate_default_contributor(apps, schema_editor):
    contributor_model = apps.get_model('api', 'contributor')
    user_1 = apps.get_model('auth', 'user').objects.all()[0]
    c = contributor_model(id=user_1.id, username=user_1.username, email=user_1.email,
                          date_joined=user_1.date_joined, client_id=uuid.uuid4())
    c.save()

class Migration(migrations.Migration):

    run_before = migrations.RunPython(migrate_default_contributor)

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
