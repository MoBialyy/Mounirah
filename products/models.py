from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    available = models.BooleanField(default=True)

    def __str__(self) :
        return self.name
    class Meta:
        verbose_name = 'Product'
    class Meta:
        ordering = ['price']