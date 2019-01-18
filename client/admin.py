from django.contrib import admin
from .models import Client, Order, OrderItem

# Register your models here.

@admin.register(Client, Order, OrderItem)
class ClientAdmin(admin.ModelAdmin):
    pass
