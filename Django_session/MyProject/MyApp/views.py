from django.shortcuts import render
from django.http import HttpResponse

def demo1(request):
    return HttpResponse("Hello from demo1 of MyApp")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")

        if uname == "Firstbit" and pwd == "admin@123":
            return HttpResponse("Login successful..")
        else:
            return HttpResponse("Login Failed..")
