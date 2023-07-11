"""
URL configuration for myinsta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from lotto.views import lotto_basic, lotto_challenge_input, lotto_challenge_output
from posts.views import url_view_http, url_view_json, url_parameter_view, function_view, index
from posts.views import class_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('lottobasic/', lotto_basic, name='lotto_basic'),
    path('lotto/input', lotto_challenge_input, name='lotto_input'),
    path('lotto/output', lotto_challenge_output, name='lotto_output'),
    path('url/http', url_view_http),
    path('url/json', url_view_json),
    path('url/query/<int:username>/', url_parameter_view),
    path('fbv/', function_view),
    path('cbv/', class_view.as_view()),

    path('', index, name='index'),
    path('posts/', include('posts.urls', namespace='posts')),
]
