from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout as auth_logout,
)
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from partner.models import Partner, Menu
from .models import Client, Order, OrderItem
# Create your views here.

URL_LOGIN = '/login/'
def client_group_check(user):
    return "client" in [ group.name for group in user.groups.all()]

def index(request):
    partner_list = Partner.objects.all()
    ctx = {
        "partner_list" : partner_list,
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
        elif group == "partner":
            partner = Partner.objects.create(
                user=user,
                name=username,
            )
            partner.is_active = False

        ctx.update({"complete" : "회원가입이 완료되었습니다."})
    return render(request, "signup.html", ctx)


def signup(request):
    ctx = {"is_client":True}
    return common_signup(request, ctx, "client")

@login_required(login_url=URL_LOGIN)
@user_passes_test(client_group_check, login_url=URL_LOGIN)
def order(request, partner_id):
    ctx = {}
    partner = Partner.objects.get(id=partner_id)
    menu_list = Menu.objects.filter(partner = partner)

    if request.method == "GET":
        ctx.update({
            "partner" : partner,
            "menu_list": menu_list,
         })
    elif request.method == "POST":
        # menu_dict = {}
        order = Order.objects.create(
            client=request.user.client,
            address="test",
        )
        for menu in menu_list:
            menu_count = request.POST.get(str(menu.id))
            # if int(menu_count) > 0 :
                # menu_dict.update({ str(menu.id) : menu_count })
            menu_count = int(menu_count)
            if menu_count > 0 :
                item = OrderItem.objects.create(
                    order=order, menu=menu, count=menu_count,
                )
                # order.items.add(item)
            return redirect("/")
    return render(request, "order_menu_list.html", ctx)

def order_list(request):
    ctx = {}

    return render(request, "order_list_for_client.html", ctx)

# def navbar_client(request):
#     ctx = {"is_client" : True}
#     return common_navbar(request, ctx, "client")
#
# def common_navbar(reqeust, ctx, group):
#     return render(request, "navbar.html", ctx)
