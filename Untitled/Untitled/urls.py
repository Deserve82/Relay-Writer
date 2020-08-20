"""Untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import Books.urls
from django.conf import settings
from django.conf.urls.static import static
import Books.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Books.views.main, name="main"),
    path('novel_list/', Books.views.novel_list, name="novel_list"),
    path('books/', include(Books.urls)),
    path('novel/<int:novel_id>', Books.views.novel, name="novel"),
    path('content/<int:novel_id>', Books.views.content, name="content"),
    path('book/<int:book_id>', Books.views.book, name="book"),
    path('book_content/<int:book_id>', Books.views.book_content, name="book_content"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

