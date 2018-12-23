from django.shortcuts import render

# Create your views here.

def signup(request):
    ctx = {}
    return render(request, "signup.html", ctx)
