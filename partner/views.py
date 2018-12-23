from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    ctx = {}
    return render(request, "index.html", ctx)

def login(request):
    if request.method == "GET":
        pass

    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/partner/")
        else:
            pass

    ctx = {}
    return render(request, "login.html", ctx)

def signup(request):
    if request.method == "GET":
        pass

    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username, email, password)

    ctx = {}
    return render(request, "signup.html", ctx)
