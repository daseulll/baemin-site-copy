from django.contrib import admin
from .models import Partner, Menu

# Register your models here.

@admin.register(Partner, Menu)
class PartnerAdmin(admin.ModelAdmin):
    pass
