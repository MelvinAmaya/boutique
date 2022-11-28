from django.test import TestCase, Client
from django.urls import reverse
from app.models import *

class TestViews(TestCase):

    def test_view(self):
        client = Client()

        response = client.get(reverse('home'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'app/home.html')