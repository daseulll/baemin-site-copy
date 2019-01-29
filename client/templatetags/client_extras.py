from django import template
from django.contrib.auth.models import Group
from client.models import Order, OrderItem

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter(name='total_price')
def total_price(value, arg):

    return value*arg
