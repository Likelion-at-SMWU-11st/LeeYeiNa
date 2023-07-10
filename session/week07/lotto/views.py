import random
from django.shortcuts import render

# Create your views here.
def lotto_basic(request):
    lotto_num = list() #로또 번호를 저장할 리스트

    #로또 번호 7자리
    for _ in range(7): #단순 반복
        lotto_num.append(random.randint(1, 45))
    
    #render : html 템플릿에 데이터(딕셔너리 형식)를 넣어 보냄
    return render(request, 'lotto_basic.html', {'lotto_num' : lotto_num })