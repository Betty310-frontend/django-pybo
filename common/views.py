from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from common.forms import UserForm


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect("common:login")


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_pwd = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_pwd)
            login(request, user)
            return redirect("index")
    else:
        form = UserForm()

    return render(request, "common/signup.html", {"form": form})


def page_not_found(request, exception):
    return render(request, "common/404.html", {})


def server_error(request):
    return render(request, "common/500.html", {})


def permission_denied(request, exception):
    return render(request, "common/403.html", {})


def bad_request(request, exception):
    return render(request, "common/400.html", {})
