from django.shortcuts import render
from django.http import HttpResponse

from .models import User

# Create your views here.
def index(request):
    return HttpResponse('all works')
# Try to use template view
def get_users(request):
    users = User.objects.all()

    return render(request, "myapp/get_users.html", {
        "users": users,
    })


def authorization(request):
    if request.method == "POST":

        name = request.POST.get("name")
        surname = request.POST.get("surname")
        nickname = request.POST.get("nickname")
        email = request.POST.get("email")
        password = request.POST.get("password")
# Modify form
        if name == "" or nickname == "" or email == "":
            raise ValueError("Value Error")

        user = User(
            name=name,
            surname=surname,
            nickname=nickname,
            email=email,
            password=password,
        ).save()

        return HttpResponse("User created")

    return render(request, "myapp/authorization.html")