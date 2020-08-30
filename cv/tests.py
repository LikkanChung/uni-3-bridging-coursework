from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from cv.views import cv
from cv.models import Contact, Education, Experience, Volunteering
import datetime

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

    def test_cv_education_model_add_full(self):
        initial_count = Education.objects.count()
        new = Education()
        new.name = "test_add_full_name"
        new.school = "test_add_full_school"
        new.location = "test_add_full_location"
        new.start_date = datetime.datetime(2019,1,1,12,0,0,0, datetime.timezone(datetime.timedelta(hours=0), name="UTC"))
        new.end_date = datetime.datetime(2020,1,1,12,0,0,0, datetime.timezone(datetime.timedelta(hours=0), name="UTC"))
        new.text = "test_add_full_text"
        new.publish()
        after_count = Education.objects.count()
        match = False
        for item in Education.objects.all():
            if item.name == new.name and item.school == new.school and item.location == new.location and item.start_date.isoformat() == new.start_date.isoformat() and item.end_date.isoformat() == new.end_date.isoformat() and item.text == new.text:
                match = True
        self.assertTrue(after_count == initial_count + 1)
        self.assertTrue(match)

    def test_cv_experience_model_add_full(self):
        initial_count = Experience.objects.count()
        new = Experience()
        new.role = "test_add_full_role"
        new.locaion = "test_add_full_location"
        new.start_date = datetime.datetime(2019,1,1,12,0,0,0, datetime.timezone(datetime.timedelta(hours=0), name="UTC"))
        new.end_date = datetime.datetime(2020,1,1,12,0,0,0, datetime.timezone(datetime.timedelta(hours=0), name="UTC"))
        new.text = "test_add_full_text"
        new.publish()
        after_count = Experience.objects.count()
        match = False
        for item in Experience.objects.all():
            if item.role == new.role and item.location == new.location and item.start_date.isoformat() == new.start_date.isoformat() and item.end_date.isoformat() == new.end_date.isoformat() and item.text == new.text:
                match = True
        self.assertTrue(after_count == initial_count + 1)
        self.assertTrue(match)

    def test_cv_vounteering_model_add_full(self):
        initial_count = Volunteering.objects.count()
        new = Volunteering()
        new.role = "test_add_full_role"
        new.locaion = "test_add_full_location"
        new.start_date = datetime.datetime(2019,1,1,12,0,0,0, datetime.timezone(datetime.timedelta(hours=0), name="UTC"))
        new.end_date = datetime.datetime(2020,1,1,12,0,0,0, datetime.timezone(datetime.timedelta(hours=0), name="UTC"))
        new.text = "test_add_full_text"
        new.publish()
        after_count = Volunteering.objects.count()
        match = False
        for item in Volunteering.objects.all():
            if item.role == new.role and item.location == new.location and item.start_date.isoformat() == new.start_date.isoformat() and item.end_date.isoformat() == new.end_date.isoformat() and item.text == new.text:
                match = True
        self.assertTrue(after_count == initial_count + 1)
        self.assertTrue(match)
