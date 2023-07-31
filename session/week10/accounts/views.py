from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('index')


def login_view(request):
    if request.method == "GET":
        # 로그인 HTML 응답
        return render(request, 'accounts/login.html', {'forms': AuthenticationForm()})
    else:
        form = AuthenticationForm(request, request.POST)  # 데이터 유효성 검사
        if form.is_valid():  # 로그인 성공
            login(request, form.user_cache)
            return redirect('index')
        else:  # 로그인 실패
            return render(request, 'accounts/login.html', {'forms': form})


def signup_view(request):
    # GET 요청 시 HTML 응답
    if request.method == "GET":
        form = SignupForm
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:  # Post 요청 시 데이터 확인 후 회원 생성
        form = SignupForm(request.POST)
        if form.is_valid():  # 회원가입 처리
            instance = form.save()
            return redirect('index')
        else:
            return redirect('accounts:signup')
