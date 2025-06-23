from django.db import models
import uuid
# Create your models here.

class Cart(models.Model):
    id = models.BigAutoField(primary_key=True),
    user_id = models.UUIDField(blank=True, null=True)

class CartItem(models.Model):
    id = models.BigAutoField(primary_key=True),
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    descripcion = models.CharField(blank=True, null=True)
