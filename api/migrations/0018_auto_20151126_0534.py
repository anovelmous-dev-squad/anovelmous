# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20151125_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterVote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('client_id', models.UUIDField(unique=True, default=uuid.uuid4)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('score', models.SmallIntegerField()),
                ('character', models.ForeignKey(to='api.Character')),
                ('contributor', models.ForeignKey(to='api.Contributor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlaceVote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('client_id', models.UUIDField(unique=True, default=uuid.uuid4)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('score', models.SmallIntegerField()),
                ('contributor', models.ForeignKey(to='api.Contributor')),
                ('place', models.ForeignKey(to='api.Place')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlotItemVote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('client_id', models.UUIDField(unique=True, default=uuid.uuid4)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('score', models.SmallIntegerField()),
                ('contributor', models.ForeignKey(to='api.Contributor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PlotVote',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('client_id', models.UUIDField(unique=True, default=uuid.uuid4)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('score', models.SmallIntegerField()),
                ('contributor', models.ForeignKey(to='api.Contributor')),
                ('plot', models.ForeignKey(to='api.Plot')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='plotitem',
            name='contributor',
            field=models.ForeignKey(related_name='plotitems', to='api.Contributor'),
        ),
        migrations.AddField(
            model_name='plotitemvote',
            name='plot_item',
            field=models.ForeignKey(to='api.PlotItem'),
        ),
    ]
