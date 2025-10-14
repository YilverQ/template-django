from django.db import models

# Create your models here.
class Product(models.Model):
    name        = models.CharField(max_length=255)
    stocks      = models.PositiveIntegerField(default=0)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    status      = models.BooleanField(default=True)
    bar_code    = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name