from django.db import models

# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="image/")
