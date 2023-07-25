from django.db import models
from django.shortcuts import render, redirect
from .forms import UserCreateForm, SignupForm
# Create your models here.


def signup_view(request):
    if request.method == "GET":
        form = UserCreateForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('index')
        else:
            return redirect('accounts:signup')
