from django.views import generic
from django.apps import apps

from base.models import Project
from crawl_space.models import Crawl
from crawl_space.forms import AddCrawlForm


class AddCrawlView(generic.edit.CreateView):
    form_class = AddCrawlForm
    template_name = "crawl_space/add_crawl.html"

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.project = Project.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)


class CrawlView(generic.DetailView):
    model = Crawl
    template_name = "crawl_space/crawl.html"
