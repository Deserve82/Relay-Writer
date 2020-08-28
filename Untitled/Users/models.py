from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class CustomUserModel(AbstractUser):
    point = models.IntegerField(null=False, default=0)
    nickname = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

# 장고에서는 user를 import를 해서 pw, user등에 대한 속성이 이미 제공되기에 나머지만 정해주면 된다.
