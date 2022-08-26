from django.db import models

# Create your models here.
class Order(models.Model):

  type = models.CharField(max_length=100, blank=False)
  price = models.PositiveIntegerField(default=1)

  condition = models.CharField(
    max_length=20,
    default = 'New',
    choices = (
      ('New', 'New'),
      ('Used', 'Used'),
    ))

  device_type = models.CharField(
  max_length=20,
  default='Desktop',
  choices=(
    ('Desktop', 'Desktop'),
    ('Laptop', 'Laptop'),
    ('Mobile', 'Mobile'),
  ))

  order_type = models.CharField(
  max_length=20,
  default='Order',
  choices=(
    ('Order', 'Order'),
    ('Notify', 'Notify'),
    ('Book', 'Book'),
  ))

  def __str__(self):
    return f'{self.model} - ${self.price}'