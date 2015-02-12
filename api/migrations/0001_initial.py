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
            name='Chapter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FormattedNovelToken',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ordinal', models.IntegerField()),
                ('content', models.CharField(max_length=35)),
                ('chapter', models.ForeignKey(to='api.Chapter')),
            ],
            options={
                'abstract': False,
                'ordering': ['ordinal'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(unique=True, max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NovelToken',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ordinal', models.IntegerField()),
                ('chapter', models.ForeignKey(to='api.Chapter')),
            ],
            options={
                'abstract': False,
                'ordering': ['ordinal'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(unique=True, max_length=28)),
                ('is_punctuation', models.BooleanField(default=False)),
                ('is_valid', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ordinal', models.IntegerField()),
                ('selected', models.BooleanField(default=False)),
                ('chapter', models.ForeignKey(to='api.Chapter')),
                ('token', models.ForeignKey(to='api.Token')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['ordinal'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='noveltoken',
            name='token',
            field=models.ForeignKey(to='api.Token'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='noveltoken',
            unique_together=set([('ordinal', 'chapter')]),
        ),
        migrations.AlterUniqueTogether(
            name='formattednoveltoken',
            unique_together=set([('ordinal', 'chapter')]),
        ),
        migrations.AddField(
            model_name='chapter',
            name='novel',
            field=models.ForeignKey(to='api.Novel', related_name='chapters'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='chapter',
            unique_together=set([('title', 'novel')]),
        ),
    ]
