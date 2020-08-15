from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from django.utils import timezone # 현재시간 저장
# from .form import (폼 class 이름)

def main(request):
    # book과 novel의 list 페이지를 서로 분리할까? 아니면 redirect 시키는 방식으로 할까?

    # main 페이지로 넘겨줘야 할 정보가 무엇이 있을까
    # 1. DB 내에 존재하는 전체 Book의 정보
    books = Book.objects.all()
    
    return render(request, 'main.html', {'books':books})


def novel(request,novel_id):
    novel = get_object_or_404(Novel, pk = novel_id)    # class이름, pk=primal key -> DB에 있는 id  # 안되면 404페이지 띄워주세요
    # 좋아요

    print(novel)
    # like_num = len(novel.like.all())
    return render(request, 'novel.html',{'novel':novel}) # 객체를 novel에 저장해주세요 -> novel을 detail1.html에 보내주세요