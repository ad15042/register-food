from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=20)
    price = models.IntegerField()
    place = models.CharField(max_length=20)
    payment_date = models.DateTimeField()
    meal_format = models.PositiveIntegerField() # 0または正の整数
    category = models.CharField(max_length=20)
    degree_regret = models.IntegerField()

    def __str__(self):
        return self.product_name


