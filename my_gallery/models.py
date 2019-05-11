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
  image = models.ImageField(upload_to='image/',default='grad.jpeg')
  name = models.CharField(max_length=40)
  description = models.TextField()
  location = models.ForeignKey(Location)
  category = models.ForeignKey(Category)

  def __str__(self):
    return self.name