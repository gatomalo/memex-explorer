# Test
from memex.test_utils.unit_test_utils import UnitTestSkeleton, form_errors
from django.test import TestCase
from django.db import IntegrityError

# App
from base.forms import AddProjectForm
from base.models import Project


class TestAddDataModelView(UnitTestSkeleton):

    @classmethod
    def setUpClass(cls):
        super(TestAddDataModelView, cls).setUpClass()
        cls.test_project = Project(
            name = "Model Test",
            description = "Test Project Description",
            icon = "fa-arrows")
        cls.test_project.save()

    @property
    def slugs(self):
        return dict(slugs=dict(
            slug="model-test"))

    def test_add_model_page(self):
        response = self.get('base:crawl_space:add_data_model', **self.slugs)
        assert 'crawl_space/add_data_model.html' in response.template_name

