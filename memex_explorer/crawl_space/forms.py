from django.forms import ModelForm, RadioSelect

from crawl_space.models import Crawl


class AddCrawlForm(ModelForm):
    class Meta:
        model = Crawl
        fields = ['name', 'description', 'crawler']
        widgets = {'crawler': RadioSelect}

