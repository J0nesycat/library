from django.contrib import admin
from django.urls import path, include
from .views import SignUpView,ProfileView,ProfileUpdateView
urlpatterns=[
    path("signup", SignUpView.as_view(), name="signup"),
    path("profile/<int:pk>",ProfileView.as_view(), name="profile_detail"),
    path("profile/<int:pk>/edit",ProfileUpdateView.as_view(), name="profile_edit")

]