from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50)
    brand = models.CharField(max_length = 50)
    description = models.TextField(null = True, blank = True)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)

    def __str__(self):
        return str(self.title)