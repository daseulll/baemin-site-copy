from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from partner.models import Partner, Menu
from .models import Client, Order
# Create your views here.

def index(request):
    partner_list = Partner.objects.all()
    ctx = {
        "partner_list" : partner_list
    }

    return render(request, "main.html", ctx)

def common_login(request, ctx, group):
    if request.method == "GET":
        pass
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            if group not in [group.name for group in user.groups.all()]:
                ctx.update({"error" : "접근 권한이 없습니다."})
                for group in user.groups.all():
                    print("group : ", group)
            else:
                auth_login(request, user)
                next_value = request.GET.get("next")
                if next_value:
                    return redirect(next_value)
                else:
                    if group == "partner":
                        return redirect("/partner/")
                    else:
                        return redirect("/")
        else:
            ctx.update({"error" : "사용자가 없습니다."})


    return render(request, "login.html", ctx)

def login(request):
    ctx = {"is_client":True}
    return common_login(request, ctx, "client")

def common_signup(request, ctx, group):
    if request.method == "GET":
        pass

    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(username, email, password)
        target_group = Group.objects.get(name=group)
        user.groups.add(target_group)

        if group == "client":
            Client.objects.create(user=user, name=username)
    return render(request, "signup.html", ctx)

def signup(request):
    ctx = {"is_client":True}
    return common_signup(request, ctx, "client")
