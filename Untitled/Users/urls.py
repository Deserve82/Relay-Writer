from django.urls import path, include
from . import views

urlpatterns = [
    path("signin", views.signin, name="signin"),
    path("logout", views.signin, name="logout"),
    path("signup", views.signup, name="signup"),
]