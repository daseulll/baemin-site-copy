from django.shortcuts import render
from partner.models import Partner, Menu
# Create your views here.

def index(request):
    partner_list = Partner.objects.all()
    ctx = {
        "partner_list" : partner_list
    }

    return render(request, "main.html", ctx)
