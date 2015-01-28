# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '__first__'),
        ('crawl_space', '0002_auto_20150128_1816'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('project', models.ForeignKey(to='base.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('data_uri', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('crawl', models.ForeignKey(to='crawl_space.Crawl')),
                ('project', models.ForeignKey(to='base.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
