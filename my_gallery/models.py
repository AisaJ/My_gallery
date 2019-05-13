from django.db import models

# Create your models here
class Location(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
    return self.name
  def save_location(self):
    self.save()

  def del_location(self):
    self.delete()

  def update_location(self):
    self.insert()

class Category(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
    return self.name
  def save_category(self):
    self.save()

  def del_category(self):
    self.delete()

  def update_category():
    self.insert()

class Image(models.Model):
  image = models.ImageField(upload_to='image/',default='children.jpg')
  name = models.CharField(max_length=40)
  description = models.TextField()
  location = models.ForeignKey(Location)
  category = models.ForeignKey(Category)

  def __str__(self):
    return self.name

  def save_image(self):
    self.save()

  def del_image(self):
    self.delete()

  def update_image(self):
    self.insert()

  @classmethod
  def search_by_category(cls,search_term):
    image_result = cls.objects.filter(category__name__icontains=search_term)
    return image_result

  @classmethod
  def filter_by_location(cls,location):
    image = cls.objects.filter(location__location=location)
    return image

  @classmethod
  def get_image_by_id(cls,id):
    image = cls.objects.get(Image.id)
    return image