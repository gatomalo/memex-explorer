# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawl_space', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datamodel',
            name='project',
        ),
        migrations.RemoveField(
            model_name='datasource',
            name='crawl',
        ),
        migrations.RemoveField(
            model_name='datasource',
            name='project',
        ),
        migrations.DeleteModel(
            name='DataSource',
        ),
        migrations.RemoveField(
            model_name='crawl',
            name='data_model',
        ),
        migrations.DeleteModel(
            name='DataModel',
        ),
        migrations.AlterField(
            model_name='crawl',
            name='harvest_rate',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crawl',
            name='pages_crawled',
            field=models.BigIntegerField(default=0),
            preserve_default=True,
        ),
    ]
