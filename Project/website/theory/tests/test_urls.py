from django.test import TestCase
from django.urls import reverse, resolve
from theory.views import home, key_detail, toggle_common


class TestUrls(TestCase):
    def test_url_home_resolved(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, home)

    def test_url_detail_resolved(self):
        url = reverse("key_detail", args=[2])
        self.assertEquals(resolve(url).func, key_detail)

    def test_url_common_resolved(self):
        url = reverse("toggle_common", args=[2, 1])
        self.assertEquals(resolve(url).func, toggle_common)
