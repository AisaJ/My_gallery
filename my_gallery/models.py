from django.db import models

# Create your models here
class Location(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
    return self.name

class Category(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
    return self.name

class Image(models.Model):
  image = models.ImageField(upload_to='image/',default='children.jpg')
  name = models.CharField(max_length=40)
  description = models.TextField()
  location = models.ForeignKey(Location)
  category = models.ForeignKey(Category)

  def __str__(self):
    return self.name

  @classmethod
  def search_by_category(cls,search_term):
    image_result = cls.objects.filter(category__name__icontains=search_term)
    return image_result
    
  @classmethod
  def search_by_location(cls,search_term):
    image_result = cls.objects.filter(location__name__icontains=search_term)
    return image_result