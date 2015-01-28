# Test
from memex.test_utils.unit_test_utils import UnitTestSkeleton
from django.test import TestCase

# App
from base.forms import AddProjectForm
from base.models import Project

def form_errors(response):
    return response.context['form'].errors


class TestViews(UnitTestSkeleton):

    def test_front_page(self):
        response = self.get('base:index')
        assert 'base/index.html' in response.template_name


    def test_about_page(self):
        response = self.get('base:about')
        assert 'base/about.html' in response.template_name


    def test_project_page(self):
        response = self.get('base:add_project')
        assert 'base/add_project.html' in response.template_name


    def test_add_project_no_name(self):
        response = self.post('base:add_project',
            {'description': 'cats cats cats',
             'icon': 'fa-arrows'})
        assert 'This field is required.' in form_errors(response)['name']


    def test_add_project_no_description(self):
        response = self.post('base:add_project',
            {'name': 'CATS',
             'icon': 'fa-arrows'})
        assert 'This field is required.' in form_errors(response)['description']


    def test_add_project(self):
        response = self.post('base:add_project',
            {'name': 'CATS',
             'description': 'cats cats cats',
             'icon': 'fa-arrows'})
        assert 'base/index.html' in response.template_name
        assert b'CATS' in response.content


    def test_add_project_with_right_slug(self):
        self.test_add_project()

        response = self.get('base:project',
            slugs=dict(slug="cats"))
        assert 'base/project.html' in response.template_name


class TestForms(TestCase):

    def test_project_form(self):
        form_data = {
            'name': 'CATS',
            'description': 'cats cats cats',
            'icon': 'fa-arrows'}
        form = AddProjectForm(data=form_data)
        assert form.is_valid()


    def test_project_form_no_name(self):
        form_data = {
            'description': 'cats cats cats',
            'icon': 'fa-arrows'}
        form = AddProjectForm(data=form_data)
        assert form.is_valid() is False
        assert 'This field is required.' in form.errors['name']


    def test_project_form_no_description(self):
        form_data = {
            'name': 'CATS',
            'icon': 'fa-arrows'}
        form = AddProjectForm(data=form_data)
        assert form.is_valid() is False
        assert 'This field is required.' in form.errors['description']


class TestDatabase(TestCase):

    def setUp(self):
        project = Project.objects.create(name="Bicycles for sale", description="Project about bicycles",
            icon="fa-bicycle")
        self.project = project

    def test_project_exists(self):
        assert Project.objects.get(name="Bicycles for sale")

    def test_get_by_slug(self):
        assert 'bicycles-for-sale' == self.project.slug

