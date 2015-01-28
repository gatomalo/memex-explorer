# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawl_space', '0003_datamodel_datasource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datamodel',
            name='project',
        ),
        migrations.DeleteModel(
            name='DataModel',
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
    ]
