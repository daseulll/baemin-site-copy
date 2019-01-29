from django.db import models
from django.contrib.auth.models import User
from partner.models import Menu

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name="고객 이름")

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(
        max_length=100, verbose_name="주소",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    items = models.ManyToManyField(
        Menu,
        through='OrderItem',
        through_fields=('order', 'menu'),
    )

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.menu.name
