from django.db import models

# Create your models here.
class Widget(models.Model):
  title = models.CharField(max_length=200)
  url = models.CharField(max_length=200)
  shorthand = models.CharField(max_length=20)
  def __str__(self):
    return(self.title)