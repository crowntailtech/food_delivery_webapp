from django.db import models
from django.contrib.auth.models import User
from address.models import Custaddress


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Custaddress, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    items = models.ManyToManyField('Product', through='OrderItem')

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} on {self.order_date}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.product.name} in Order #{self.order.id}"