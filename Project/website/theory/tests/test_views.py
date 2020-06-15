from django.test import TestCase, Client
from django.urls import reverse
from theory.models import Key
import json


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home = reverse("home")
        self.key_detail = reverse("key_detail", args=[1])
        self.toggle_common = reverse("toggle_common", args=[1, 1])
        self.key1 = Key.objects.create(name="D")

    def test_home_view(self):

        response = self.client.get(self.home)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_detail_view(self):

        response = self.client.get(self.key_detail)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "key_detail.html")

    def test_toggle_common_view(self):

        response = self.client.get(self.toggle_common)

        self.assertEquals(response.status_code, 302)
