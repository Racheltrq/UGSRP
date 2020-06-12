from django.test import TestCase, Client
from django.urls import reverse
from theory.models import Key
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home = reverse('home')
        self.key_detail = reverse('key_detail', args=[1])
        self.common = reverse('common', args=[1])
        self.notcommon = reverse('notcommon', args=[1])
        self.key1 = Key.objects.create(
            name = 'D'
        )


    def test_home_view(self):

        response = self.client.get(self.home)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


    def test_detail_view(self):

        response = self.client.get(self.key_detail)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'key_detail.html')


    def test_common_view(self):

        response = self.client.get(self.common)

        self.assertEquals(response.status_code, 302)



    def test_notcommon_view(self):

        response = self.client.get(self.notcommon)

        self.assertEquals(response.status_code, 302)
