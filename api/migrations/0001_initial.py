# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampedModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NovelToken',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(serialize=False, to='api.TimeStampedModel', auto_created=True, parent_link=True, primary_key=True)),
                ('ordinal', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('api.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(serialize=False, to='api.TimeStampedModel', auto_created=True, parent_link=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=('api.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='FormattedNovelToken',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(serialize=False, to='api.TimeStampedModel', auto_created=True, parent_link=True, primary_key=True)),
                ('ordinal', models.IntegerField()),
                ('token', models.CharField(max_length=35)),
            ],
            options={
                'abstract': False,
            },
            bases=('api.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(serialize=False, to='api.TimeStampedModel', auto_created=True, parent_link=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('novel', models.ForeignKey(to='api.Novel')),
            ],
            options={
            },
            bases=('api.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(serialize=False, to='api.TimeStampedModel', auto_created=True, parent_link=True, primary_key=True)),
                ('content', models.CharField(unique=True, max_length=28)),
                ('is_punctuation', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=('api.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(serialize=False, to='api.TimeStampedModel', auto_created=True, parent_link=True, primary_key=True)),
                ('ordinal', models.IntegerField()),
                ('selected', models.BooleanField(default=False)),
                ('chapter', models.ForeignKey(to='api.Chapter')),
                ('token', models.ForeignKey(to='api.Token')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=('api.timestampedmodel',),
        ),
        migrations.AddField(
            model_name='noveltoken',
            name='chapter',
            field=models.ForeignKey(to='api.Chapter'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='noveltoken',
            name='token',
            field=models.ForeignKey(to='api.Token'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='formattednoveltoken',
            name='chapter',
            field=models.ForeignKey(to='api.Chapter'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together=set([('title', 'novel')]),
        ),
    ]
