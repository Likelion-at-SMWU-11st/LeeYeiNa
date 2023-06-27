from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def study_func(request):
    return render(request, 'stst.html')  # stst.html 파일 렌더링
