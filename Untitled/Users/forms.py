# from django import forms
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class LoginForm(AuthenticationForm):
#     pass

# class RegisterForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ["username", "password1","password2","email", "birthday", "gender"]
# #models.py에서 테이블 만들고 views에서 모두 처리하는것 중간에 forms.py를 이용하면 필터링역할을 해줄 수 있다. 

from django import forms

from .models import CustomUserModel


# from django.contrib.auth.models import User
# 어스에서 제공하는 유저 모델을 가져오겠다.


class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'password']

        help_texts = {
            'username': None,
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:shadow-outline-blue focus:border-blue-300 focus:z-10 sm:text-sm sm:leading-5'}),
            'password': forms.TextInput(attrs={
                'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:shadow-outline-blue focus:border-blue-300 focus:z-10 sm:text-sm sm:leading-5'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'email', 'password', 'nickname', 'phone_number']
        help_texts = {
            'username': None,
        }

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:shadow-outline-blue focus:border-blue-300 focus:z-10 sm:text-sm sm:leading-5'}),
            'email': forms.EmailInput(attrs={
                'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:shadow-outline-blue focus:border-blue-300 focus:z-10 sm:text-sm sm:leading-5'}),
            'password': forms.TextInput(attrs={
                'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:shadow-outline-blue focus:border-blue-300 focus:z-10 sm:text-sm sm:leading-5'}),
            'nickname': forms.TextInput(attrs={
                'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:shadow-outline-blue focus:border-blue-300 focus:z-10 sm:text-sm sm:leading-5'}),
            'phone_number': forms.TextInput(attrs={
                'class': 'appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:shadow-outline-blue focus:border-blue-300 focus:z-10 sm:text-sm sm:leading-5'}),
        }
