from django.test import TestCase


class SmokeTests(TestCase):
    def test_landing_loads(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
