from rest_framework.test import APIClient
from django.test import SimpleTestCase
from django.urls import reverse


class BaseSimpleTestCase(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        cls.api_client = APIClient()

    def prepare_urls(self):
        self.user_details = reverse('django_app: My_Post_Call')


