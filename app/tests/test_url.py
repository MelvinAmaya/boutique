from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import*

class Testurls(SimpleTestCase):

    def test_url(self):
      url= reverse('registrar')
      print(resolve(url))
      self.assertEquals(resolve(url).func,registro)