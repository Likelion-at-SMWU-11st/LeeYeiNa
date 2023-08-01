from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager


# Create your models here.

# 장고 모델이 쿼리를 날릴 때 제공해주는 인터페이스
class UserManager(DjangoUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError('이메일은 필수 값입니다.')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # 비밀번호를 암호화(해싱)해서 저장
        user.save(using=self._db)  # 사용자 저장
        return user

    # 일반 사용자
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self.create_user(username, email, password, **extra_fields)

    # 관리자
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    # 기존 모델에 전화번호 필드 추가
    phone = models.CharField(verbose_name="전화번호", max_length=11)
    objects = UserManager()


class UserInfo(models.Model):
    phone_sub = models.CharField(verbose_name='보조 전화번호', max_length=11)
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
