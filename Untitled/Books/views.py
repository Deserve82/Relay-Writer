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

def update_novel(request, novel_id):
    update_novel = get_object_or_404(Novel, id = novel_id)
    update_novel.title = request.POST['title']
    update_novel.writingDate = request.POST['writingDate']
    update_novel.novelPrice = request.POST['novelPrice']
    update_novel.novelContent = request.POST['novelContent']
    # relay_writer.cateogory = request.GET['new_category']
    update_novel.save()
    return redirect('/books/'+str(update_novel.id))
    