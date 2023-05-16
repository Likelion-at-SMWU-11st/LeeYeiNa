from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def helloBabyLion(rerquest): #request 받아서
    return HttpResponse("Hello DJango")