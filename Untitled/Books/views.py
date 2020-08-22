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
    update_novel.save()
    return redirect('/books/'+str(update_novel.id))
    

def novel(request,novel_id):
    novel = get_object_or_404(Novel, pk = novel_id)    # class이름, pk=primal key -> DB에 있는 id  # 안되면 404페이지 띄워주세요
    tags = Tag.objects.filter(novel=novel)

    print(novel)
    # like_num = len(novel.like.all())
    return render(request, 'novel.html',{'novel':novel,'tags':tags}) # 객체를 novel에 저장해주세요 -> novel을 detail.html에 보내주세요

def tagging(request, novel_id):
    new_tag = Tag()
    new_tag.novel = get_object_or_404(Novel, pk = novel_id)
    new_tag.body = request.POST.get('body')
    new_tag.save()
    return redirect('/novel/' + str(novel_id))

def content(request,novel_id):
    novel = get_object_or_404(Novel, pk = novel_id)
    return render(request, 'content.html',{'novel':novel})
