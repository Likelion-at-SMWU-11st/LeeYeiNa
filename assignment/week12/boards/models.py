from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Board (models.Model):
    content = models.TextField(verbose_name='내용', null=True)
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
