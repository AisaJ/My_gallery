from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class ImageTestClass(TestCase):
  #Set up method
  def setUp(self):
    self.kids_weekend = Image(image ='sneakers.jpeg',name='Sneakers',description='Bright colored and light')

  #Testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.kids_weekend,Image))

