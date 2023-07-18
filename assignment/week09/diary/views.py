from django.shortcuts import render
from django.views.generic import ListView
from .models import contents

# Create your views here.


class class_view(ListView):
    model = contents
    template_name = 'today.html'


def write(request):
    return render(request, 'diary_write.html')
