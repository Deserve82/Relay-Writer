from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.utils import timezone
from .form import WriteForm

def main(request):
    # book과 novel의 list 페이지를 서로 분리할까? 아니면 redirect 시키는 방식으로 할까?

    # main 페이지로 넘겨줘야 할 정보가 무엇이 있을까
    # 1. DB 내에 존재하는 전체 Book의 정보
    books = Book.objects.all()
    
    return render(request, 'main.html', {'books':books})

def new(request):
    if request.method == "POST":
        form = WriteForm(request.POST, request.FILES)
        if form.is_valid():
            novel = form.save(commit = False)
            novel.save()
            return redirect('')
    else:
        form = WriteForm()
        return render(request, 'new.html', {'form' : form})

def update(request):
    update = Novel
    update.title = request.GET['title']
    update.writingDate = request.GET['writingDate']
    update.novelPrice = request.GET['novelPrice']
    update.novelContent = 'novelContent' in request.POST
    # relay_writer.cateogory = request.GET['new_category']
    return redirect('/Books/'+str(update.id))
    