from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.new, name='new'),
    path('update/<int:novel_id>', views.update, name='novel_update'),
    path('profile/', views.profile, name='profile'),

]
