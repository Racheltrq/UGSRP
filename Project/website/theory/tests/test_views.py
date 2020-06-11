from django.test import TestCase, Client
from django.urls import reverse
from theory.models import Key
import json

class TestViews(TestCase):
    def test(self):
        client = Client()

        response = client.get(reverse('home'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
