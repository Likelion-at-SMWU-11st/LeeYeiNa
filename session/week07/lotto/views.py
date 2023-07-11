import random
from django.shortcuts import render

# Create your views here.


def lotto_basic(request):
    lotto_num = list()  # 로또 번호를 저장할 리스트

    # 로또 번호 7자리
    for _ in range(7):  # 단순 반복
        lotto_num.append(random.randint(1, 45))

    # render : html 템플릿에 데이터(딕셔너리 형식)를 넣어 보냄
    return render(request, 'lotto_basic.html', {'lotto_num': lotto_num})


def lotto_challenge_input(request):
    return render(request, 'lotto_challenge_input.html')


def lotto_challenge_output(request):
    lotto_num = list()
    game = request.GET.get('game', 1)

    for _ in range(int(game)):
        temp = list()
        for _ in range(7):
            temp.append(random.randint(1, 45))
        lotto_num.append(temp)
    '''
    pull number = [index for index in range(1, 46)]
    for _ in range(int(game)):
        lotto_num.append(random.sample(pull_number, 6)) #pull number에서 6번 random하게 뽑기
    '''
    return render(request, 'lotto_challenge_output.html', {'game': game, 'lotto_num': lotto_num})
