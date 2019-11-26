from django.urls import resolve
from django.test import TestCase
from .views import home_page


class HomePageTest(TestCase):

    def test_rool_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
