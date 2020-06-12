from django.test import TestCase, Client
from django.urls import reverse
from theory.models import Key
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home = reverse('home')
        


    def test_home_view(self):

        response = self.client.get(self.home)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
