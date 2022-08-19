from django.db import models

# Create your models here.
class Device(models.Model):
  type = models.CharField(max_length=100, blank=False)
  issues = models.CharField(max_length=100, default='No issues')
  description = models.TextField(max_length=100, blank=True)

  condition = models.CharField(
    max_length=20,
    default = 'New',
    choices = (
      ('New', 'New'),
      ('Used', 'Used'),
    ))

  status = models.CharField(
    max_length=20,
    default = 'Sold',
    choices = (
      ('Sold', 'Sold'),
      ('Available', 'Available'),
      ('Restocking', 'Restocking'),
    ))

  price = models.PositiveIntegerField(default=1)

  class Meta:
    abstract = True #avoids making new models for this class 

  def __str__(self):
    '''Returns string representation of the Device model'''
    return f'{self.type} - ${self.price}'

class Laptop(Device):
  '''Inherits from the Device model'''
  pass

class Desktop(Device):
  '''Inherits from the Device model'''
  pass

class Mobile(Device):
  '''Inherits from the Device model'''
  pass