from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4
from django.utils import timezone
import datetime

def date_upload_to(instance, filename):
  # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
  
  ymd_path = timezone.now().strftime('%Y/%m/%d') 
  uuid_name = uuid4().hex
  extension = os.path.splitext(filename)[-1].lower()
  return '/'.join([
    ymd_path,
    uuid_name + extension,
  ])

# Create your models here.
class Comment(models.Model):
    pass
    

class Rate(models.Model):
    pass
    

class Novel(models.Model):
    category = (                    # novel 카테고리
                ("세계문학전집"),
                ("인문"),
                ("철학"),
                ("사회"),
                ("에세이"),
                ("과학"),
                ("역사"),
                ("경제경영"),
                ("자기계발"),
                ("여행"),
                ("라이프스타일"),
                ("부모"),
                ("어린이/청소년"),
                ("종교"),
                ("판타지/무협"),
                ("로맨스"),
                ("만화"),
                ("애니메이션"),
    )
    title = models.CharField(max_length=30)        # novel 제목 # max_length=30으로 변경
    author = models.CharField(max_length=30)       # novel 저자 -> book은 엮은 이가 무조건 User기 때문에 문제가 없늗데, novel은 저자가 User가 아닌 고전 작가일수도, User일수도 있지 않나? 그럼 우카징ㅠ
    publisher = models.CharField(max_length=30)    # novel 출판사 -> 없을 수도 있음
    writingDate = models.DateField(default=datetime.date.today)                                         # novel 작성일
    novelImage = models.ImageField(upload_to="novel/")        # novel 표지
    novelPrice = models.IntegerField(null = True,default=0)                  # novel 가격
    novelContent = models.TextField()                                        # novel 내용
    # noveltag = models.CharField(max_length=15)
    # 

class Book(models.Model):
    category = (                    # book 카테고리
                ("세계문학전집"),
                ("인문"),
                ("철학"),
                ("사회"),
                ("에세이"),
                ("과학"),
                ("역사"),
                ("경제경영"),
                ("자기계발"),
                ("여행"),
                ("라이프스타일"),
                ("부모"),
                ("어린이/청소년"),
                ("종교"),
                ("판타지/무협"),
                ("로맨스"),
                ("만화"),
                ("애니메이션"),
    )
    title = models.CharField(max_length=150)                            # book 제목
    editor = models.ForeignKey(User, on_delete=models.CASCADE)          # 엮은이
    editDate = models.DateField()                                       # book 엮은 날짜
    bookImage = models.ImageField(upload_to="book/")      # book 표지
    bookPrice = models.IntegerField(null = True,default=0)              # book 가격
    contents = models.ManyToManyField(Novel)                            # book의 구성 내용 : book - novel을 이어주는 m:n