from django.shortcuts import render, redirect
from .forms import UserCreateForm, SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.


def logout_view(request):
    if request.user.is_authenticatd:
        logout(request)

    return redirect('index')


def login_view(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html', {'forms': AuthenticationForm()})
    else:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html', {'forms': form})


def signup_view(request):
    if request.method == "GET":
        form = SignupForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('index')
        else:
            return redirect('accounts:signup')
