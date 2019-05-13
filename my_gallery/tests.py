from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class GalleryTestClass(TestCase):
  #Set up method and saving instances
  def setUp(self):
    #location
    self.mombasa = Location(name='Mombasa')
    self.mombasa.save()
    #category
    self.sports = Category(name='Sports')
    self.sports.save()
    #image
    self.kids_weekend = Image(image ='sneakers.jpeg',name='Sneakers',description='Bright colored and light',category=self.sports,location=self.mombasa)
    self.kids_weekend.save()
    
  #Testing instance
  def test_instance(self):
    self.assertTrue(isinstance(self.kids_weekend,Image))
    self.assertTrue(isinstance(self.mombasa,Location))
    self.assertTrue(isinstance(self.sports,Category))

  #Destroying the instance after test
  def tearDown(self):
    Image.object.all().delete()
    Location.object.all().delete()
    Category.object.all().delete()

  def delete_item(self):
    self.mombasa.save()
    test_location = Location('mombasa')
    test_location.save_location
    self.mombasa.delete()
    self.assertEqual(len(Location.name),1)

  def test_search_by_category(self):
    self.kids_weekend.save()
    instance= Category.objects.get(name=='sports')
    self.assertTrue(instance.name=='sports')
