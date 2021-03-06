from django.test import TestCase
from ..models import Key


class RedirectTestCase(TestCase):
    def test_common(self):
        key = Key(name="testkey", type="maj", s_f="sharp", common=False)
        print("Before:", key.common)
        key.save()
        self.client.get("/theory/1/common/")
        key = Key.objects.get(id=1)
        print("After:", key.common, key)
        self.assertEqual(key.common, False)
