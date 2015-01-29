import os

from django.db import models
from base.models import Project
from django.utils.text import slugify
from django.core.urlresolvers import reverse

# class DataModel(models.Model):
#     name = models.CharField(max_length=64)
#     project = models.ForeignKey(Project)

#     def __str__(self):
#         return self.name

from django.conf import settings as app_settings

class Crawl(models.Model):

    def get_upload_path(instance, filename):
        return os.path.join(instance.slug, filename)

    def get_seeds_upload_path(instance, filename):
        return os.path.join(instance.slug, 'seeds', filename)

    CRAWLER_CHOICES = (
        ('nutch', "Nutch"),
        ('ache', "ACHE"))

    name = models.CharField(max_length=64, unique=True)
    slug = models.CharField(max_length=64)
    description = models.TextField()
    crawler = models.CharField(max_length=64,
        choices=CRAWLER_CHOICES,
        default='nutch')
    status = models.CharField(max_length=64)
    config = models.CharField(max_length=64)
    seeds_list = models.FileField(upload_to=get_seeds_upload_path)
    pages_crawled = models.BigIntegerField(default=0)
    harvest_rate = models.FloatField(default=0)
    project = models.ForeignKey(Project)
    # data_model = models.ForeignKey(DataModel)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Crawl, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('base:crawl_space:crawl',
            kwargs=dict(slug=self.project.slug, crawl_slug=self.slug))

