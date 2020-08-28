from django.shortcuts import render, redirect, get_object_or_404

from .form import WriteForm
from .models import *


def main(request):
    # book과 novel의 list 페이지를 서로 분리할까? 아니면 redirect 시키는 방식으로 할까?

    # main 페이지로 넘겨줘야 할 정보가 무엇이 있을까
    # 1. DB 내에 존재하는 전체 Book의 정보
    books = Book.objects.all()
    count = 0
    categories = []
    for i in Book.category:
        categories.append(Book.category[count][0])
        count = count + 1

    return render(request, 'main.html', {'books': books, 'categories': categories})


def novel_list(request):
    novels = Novel.objects.all()
    count = 0
    categories = []
    for i in Novel.category:
        categories.append(Novel.category[count][0])
        count = count + 1

    return render(request, 'novel_list.html', {'novels': novels, 'categories': categories})


# like 추가
def like(request, novel_id):
    novel = get_object_or_404(Novel, pk=novel_id)
    novel.like.add(request.user)
    novel.save()

    return redirect('/novel/' + str(novel_id))


def new(request):
    if request.method == "POST":
        form = WriteForm(request.POST, request.FILES)
        if form.is_valid():
            novel = form.save(commit=False)
            novel.save()
            return redirect('main')
        else:
            return HttpResponse('novel is not valid')
    else:
        form = WriteForm()
        return render(request, 'new.html', {'form': form})


def update(request, novel_id):
    update_novel = get_object_or_404(Novel, pk=novel_id)
    update_novel.title = request.POST['title']
    update_novel.novelImage = request.FILES['novelImage']
    update_novel.writingDate = request.POST['writingDate']
    update_novel.novelPrice = request.POST['novelPrice']
    update_novel.novelContent = request.POST['novelContent']
    update_novel.save()
    return redirect('/novel/' + str(update_novel.id))


def novel(request, novel_id):
    novel = get_object_or_404(Novel, pk=novel_id)  # class이름, pk=primal key -> DB에 있는 id  # 안되면 404페이지 띄워주세요
    tags = Tag.objects.filter(novel=novel)

    like_num = len(novel.like.all())
    return render(request, 'novel.html',
                  {'novel': novel, 'tags': tags, 'likes': like_num})  # 객체를 novel에 저장해주세요 -> novel을 detail.html에 보내주세요


def tagging(request, novel_id):
    new_tag = Tag()
    new_tag.novel = get_object_or_404(Novel, pk=novel_id)
    new_tag.body = request.POST.get('body')
    new_tag.save()
    return redirect('/novel/' + str(novel_id))


def content(request, novel_id):
    novel = get_object_or_404(Novel, pk=novel_id)
    return render(request, 'content.html', {'novel': novel})


def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)  # class이름, pk=primal key -> DB에 있는 id  # 안되면 404페이지 띄워주세요
    # 좋아요

    print(book)
    # like_num = len(novel.like.all())
    return render(request, 'book.html', {'book': book})  # 객체를 novel에 저장해주세요 -> novel을 detail.html에 보내주세요


def book_content(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'book_content.html', {'book': book})


def get_queryset(self):
    return Novel.objects.filter(tags__name=self.kwargs.get('tag'))
    # Novel 뿐만이 아니라 Book도 받아오려면 여기를 손보면 될듯!


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['tagname'] = self.kwargs['tag']
    return context


def novel_category(request):
    category = request.GET.get('q')
    novels = Novel.objects.all()
    sieved_novels = []
    for novel in novels:
        if novel.novelCategory == category:
            sieved_novels.append(novel)

    return render(request, 'novel_category.html', {'category': category, 'sieved_novels': sieved_novels})


def book_category(request):
    category = request.GET.get('q')
    books = Book.objects.all()
    sieved_books = []
    for book in books:
        if book.bookCategory == category:
            sieved_books.append(book)

    return render(request, 'book_category.html', {'category': category, 'sieved_books': sieved_books})


def profile(request):
    username = request.GET.get('username')
    if username == None or username == "":
        username = request.user.username
    novels = Novel.objects.all()
    result = []
    return render(request, 'profile.html', {'result' : result, 'username': username})
