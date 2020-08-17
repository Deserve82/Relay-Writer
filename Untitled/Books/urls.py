from django.urls import path, include
import Books.urls
from . import views

urlpatterns = [
    path('new/', views.new, name = 'new'),
    path('new_update/', views.new_update, name = "new_update"),
]