from django.shortcuts import render
from .models import *

def main(request):
    # book과 novel의 list 페이지를 서로 분리할까? 아니면 redirect 시키는 방식으로 할까?

    # main 페이지로 넘겨줘야 할 정보가 무엇이 있을까
    # 1. DB 내에 존재하는 전체 Book의 정보
    books = Book.objects.all()
    
    return render(request, 'main.html', {'books':books})