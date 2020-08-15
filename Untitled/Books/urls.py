from django.urls import path, include
import Books.urls
from . import views

urlpatterns = [
    path('new/', views.new, name = 'new'),
    path('update/', views.update, name = "update"),
]