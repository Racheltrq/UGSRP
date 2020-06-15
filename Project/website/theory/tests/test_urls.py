from django.test import TestCase
from django.urls import reverse, resolve
from theory.views import home, key_detail, common, notcommon


class TestUrls(TestCase):
    def test_url_home_resolved(self):
        url = reverse("home")
        self.assertEquals(resolve(url).func, home)

    def test_url_detail_resolved(self):
        url = reverse("key_detail", args=[2])
        self.assertEquals(resolve(url).func, key_detail)

    def test_url_common_resolved(self):
        url = reverse("common", args=[2])
        self.assertEquals(resolve(url).func, common)

    def test_url_uncommon_resolved(self):
        url = reverse("notcommon", args=[2])
        self.assertEquals(resolve(url).func, notcommon)
