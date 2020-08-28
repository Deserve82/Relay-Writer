from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.new, name='new'),
    path('update/<int:novel_id>', views.update, name='novel_update'),
    path('compile/', views.compile_book, name='compile_book'),
    path('profile/', views.profile, name='profile'),

]
