from django.views import generic
from django.apps import apps

from base.models import Project
from crawl_space.models import Crawl
from crawl_space.forms import AddCrawlForm, AddDataModelForm


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

    def get_object(self):
        return Crawl.objects.get(
            project=Project.objects.get(slug=self.kwargs['slug']),
            slug=self.kwargs['crawl_slug'])


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['project'] = self.object.project
        return context


class AddDataModelView(generic.edit.CreateView):
    form_class = AddDataModelForm
    template_name = "crawl_space/add_data_model.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.project = Project.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)

