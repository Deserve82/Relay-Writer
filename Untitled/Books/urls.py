from django.urls import path, include
import Books.urls
from . import views
from django.contrib import admin

urlpatterns = [
    path('<int:novel_id>', views.novel, name = "novel"),
]