from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView,UpdateView
from .models import Profile

# Create your views here.
class SignUpView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy("login")
    template_name="registration/signup.html"

class ProfileView(LoginRequiredMixin,DetailView):
    model= Profile
    template_name= "registration/profile_detail.html" 

class ProfileUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model= Profile
    template_name= "profile_edit.html"
    fields = ["user", "bio","location","role"]

    def test_func(self) -> bool | None:
        obj= self.get_object()
        return obj.user == self.request.user