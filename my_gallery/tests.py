from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class GalleryTestClass(TestCase):
  #Set up method
  def setUp(self):
    self.kids_weekend = Image(image ='sneakers.jpeg',name='Sneakers',description='Bright colored and light')
    self.mombasa = Location(name='Mombasa')
    self.sports = Category(name='Sports')

  #Testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.kids_weekend,Image))
    self.assertTrue(isinstance(self.mombasa.Location))
    self.assertTrue(isinstance(self.sports.Category))

  #Testing Save Method
  def test_save_method(self):
    self.kids_weekend.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images > 0))
