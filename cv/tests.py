from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from cv.views import cv
from cv.models import Contact, Education, Experience, Volunteering

class CVTest(TestCase):
    def test_cv_url_resolves_to_cv_view(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv)

    def test_cv_url_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/cv.html')

    def test_cv_url_uses_base_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'base.html')

    def test_cv_view_returns_correct_html(self):
        #Testing it has 'CV' in the title
        request = HttpRequest()
        response = cv(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>CV', html)

    def test_cv_contact_model_add_full(self):
        initial_count = Contact.objects.count()
        new = Contact()
        new.type = "test_add_full_type"
        new.detail = "test_add_full_detal"
        new.publish()
        after_count = Contact.objects.count()
        match = False
        for item in Contact.objects.all():
             if item.type == new.type and item.detail == new.detail:
                 match = True
        self.assertTrue(after_count == initial_count + 1)
        self.assertTrue(match)

    # TODO: add more rest cases
