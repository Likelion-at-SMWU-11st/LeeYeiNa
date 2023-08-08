from django.shortcuts import render
from django.contrin.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decoratoes import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['POST'])
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user.is_authenticatd:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response(status=401)
