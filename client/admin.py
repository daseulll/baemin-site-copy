from django.contrib import admin
from .models import Client, Order

# Register your models here.

@admin.register(Client, Order)
class ClientAdmin(admin.ModelAdmin):
    pass
