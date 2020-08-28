from django.urls import path, include
import Books.urls
from . import views
from django.contrib import admin

urlpatterns = [
    path('new/', views.new, name = 'new'),
    path('update/<int:novel_id>', views.update, name = 'novel_update'),
    path('profile/', views.profile, name = 'profile'),
    
]