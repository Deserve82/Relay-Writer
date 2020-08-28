from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import SigninForm, UserForm
from .models import CustomUserModel


# Create your views here.

def signin(request):
    if request.method == "POST":
        # 접근하는 방식이 포스트면
        username = request.POST['username']
        password = request.POST['password']
        # 우리가 만든 변수 그 값을 찾아서 이 변수에 대입한다.
        user = authenticate(username=username, password=password)
        # authenticate 값을 인증하고, 우리가 만든 user에 값을 대입함
        if user is not None:  # 유저 생성에 성공했나? 안했나에 대해 조건문으로 대입하고
            login(request, user)
            return redirect('/')
        else:  # 실패했다면 아래의 문자열을 보여줌
            return HttpResponse("로그인 실패")
    else:
        signin_form = SigninForm
        return render(request, 'signin.html', {'signin_form': signin_form})


def logout_view(request):
    logout(request)
    return redirect('signin')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = CustomUserModel.objects.create_user(username=form.cleaned_data['username'],
                                                           email=form.cleaned_data['email'],
                                                           password=form.cleaned_data['password'],
                                                           nickname=form.cleaned_data['nickname'],
                                                           phone_number=form.cleaned_data['phone_number'])
            login(request, new_user)
            return redirect('signin')
    else:
        form = UserForm()
        return render(request, 'signup.html', {'form': form})
