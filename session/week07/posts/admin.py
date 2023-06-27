from django.contrib import admin
from .models import Post  # models.py import
from .models import MyPage

# Register your models here.
admin.site.register(Post)  # Admin 사이트에 Post 모델 추가
admin.site.register(MyPage)  # MyPage 모델 추가
