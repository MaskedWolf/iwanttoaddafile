from django.db import models

# Create your models here.
class Category(models.Model):
  def __str__(self):
    return self.name
  name = models.CharField(max_length=255)


class State(models.Model):
  def __str__(self):
    return self.name
  name = models.CharField(max_length=255)


class Activity(models.Model):
  def __str__(self):
    return self.shopname

  username = models.CharField(max_length=255)
  shopname = models.CharField(max_length=255)
  descriptions = models.CharField(max_length=4000)
  category = models.ManyToManyField('Category', related_name='activity')
  state = models.ManyToManyField('State', related_name='activity')
  image = models.ImageField(upload_to='picture/')

  created_on = models.DateTimeField(auto_now_add=True)
  last_modified = models.DateTimeField(auto_now=True)
