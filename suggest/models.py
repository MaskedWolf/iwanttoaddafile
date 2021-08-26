from django.db import models

class suggestion(models.Model):
  place = models.IntegerField(default=0)
  name = models.CharField(max_length=200)
  link = models.CharField(max_length=200)

  def __str__(self):
    return str(self.place)

# Create your models here.
