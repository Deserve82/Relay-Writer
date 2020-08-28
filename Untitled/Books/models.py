import datetime

from django.conf import settings
from django.db import models


class Novel(models.Model):
    category = (
        ("세계문학전집", "세계문학전집"),
        ("인문", "인문"),
        ("철학", "철학"),
        ("종교", "종교"),
        ("사회", "사회"),
        ("에세이", "에세이"),
        ("과학", "과학"),
        ("역사", "역사"),
        ("경제경영", "경제경영"),
        ("자기계발", "자기계발"),
        ("여행", "여행"),
        ("라이프스타일", "라이프스타일"),
        ("부모", "부모"),
        ("어린이와청소년", "어린이와청소년"),
        ("판타지와무협", "판타지와무협"),
        ("로맨스", "로맨스"),
        ("만화", "만화"),
        ("애니메이션", "애니메이션"),
    )
    title = models.CharField(max_length=30)  # novel 제목 # max_length=30으로 변경
    author = models.CharField(
        max_length=30)  # novel 저자 -> book은 엮은 이가 무조건 User기 때문에 문제가 없늗데, novel은 저자가 User가 아닌 고전 작가일수도, User일수도 있지 않나? 그럼 우카징ㅠ
    publisher = models.CharField(max_length=30)  # novel 출판사 -> 없을 수도 있음
    writingDate = models.DateField(default=datetime.date.today)  # novel 작성일
    novelImage = models.ImageField(upload_to="novel/")  # novel 표지
    novelPrice = models.IntegerField(null=True, default=0)  # novel 가격
    novelContent = models.TextField()  # novel 내용
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likers')
    novelCategory = models.CharField(max_length=50, choices=category, default='')  # novel 카테고리


class Tag(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE, related_name='tags')
    body = models.CharField(max_length=15)
    # 15자 제한 안된다 ㅠㅠㅠㅠ
    pub_date = models.DateTimeField(auto_now_add=True)
    # 날짜는 없는 게 더 간결해서 안쓴다


class Book(models.Model):
    category = (
        ("세계문학전집", "세계문학전집"),
        ("인문", "인문"),
        ("철학", "철학"),
        ("종교", "종교"),
        ("사회", "사회"),
        ("에세이", "에세이"),
        ("과학", "과학"),
        ("역사", "역사"),
        ("경제경영", "경제경영"),
        ("자기계발", "자기계발"),
        ("여행", "여행"),
        ("라이프스타일", "라이프스타일"),
        ("부모", "부모"),
        ("어린이와청소년", "어린이와청소년"),
        ("판타지와무협", "판타지와무협"),
        ("로맨스", "로맨스"),
        ("만화", "만화"),
        ("애니메이션", "애니메이션"),
    )  # category 페이지의 url을 위해서 "어린이/청소년" -> "어린이와청소년"으로 변경했다.
    # 인자를 넘겨줄 때, regex로 "/"를 "_"로 변경할 수는 없을까? import re 해서 .replace("/", "_") 하면 되긴 하는데 어떻게 적용해야 하는지 모르겠다ㅠㅠ
    title = models.CharField(max_length=150)  # book 제목
    bookCategory = models.CharField(max_length=50, choices=category, default='')  # book 카테고리
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 엮은이
    editDate = models.DateField()  # book 엮은 날짜
    bookImage = models.ImageField(upload_to="book/")  # book 표지
    bookPrice = models.IntegerField(null=True, default=0)  # book 가격
    contents = models.ManyToManyField(Novel)  # book의 구성 내용 : book - novel을 이어주는 m:n
