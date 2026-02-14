from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from users import models

class poll_list(ListView):
    model = models.Poll
    context_object_name = "Polls"
    template_name = "users/poll.html"

class poll_detail(LoginRequiredMixin ,DetailView):
    model = models.Poll
    context_object_name = "Poll_deteil"
    template_name = "users/poll.html"

class poll_create(LoginRequiredMixin, CreateView):
    model = models.Poll
    context_object_name = "Poll_create"
    template_name = "users/poll.html"




    

# Create your views here.
