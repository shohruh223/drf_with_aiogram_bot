from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=155)
    photo = models.CharField(max_length=80)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.title
