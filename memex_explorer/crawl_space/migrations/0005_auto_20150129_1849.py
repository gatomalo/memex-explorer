# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import crawl_space.models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl_space', '0004_auto_20150128_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crawl',
            name='crawler',
            field=models.CharField(default='nutch', max_length=64, choices=[('nutch', 'Nutch'), ('ache', 'ACHE')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crawl',
            name='name',
            field=models.CharField(unique=True, max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='crawl',
            name='seeds_list',
            field=models.FileField(upload_to=crawl_space.models.Crawl.get_seeds_upload_path),
            preserve_default=True,
        ),
    ]
