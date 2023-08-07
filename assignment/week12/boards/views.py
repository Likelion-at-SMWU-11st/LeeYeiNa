from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Board
from .serializers import BoardModelSerializer
# Create your views here.


class BoardModelViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardModelSerializer
