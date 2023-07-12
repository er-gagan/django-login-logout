from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def handleLoginForm(request):
    if request.user.is_authenticated:
        return redirect("/public")
    return render(request, "login.html")


def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/welcome')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})

    return redirect("/")


def handleWelcome(request):
    if request.user.is_authenticated:
        return render(request, "welcome.html")
    return redirect("/")


def handleLogout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")
