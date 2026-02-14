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


# class poll_vote

# class poll_result

class portfolio_list(ListView):
    model = models.Portfolio
    context_object_name = "Portfolio"
    template_name = "user/portfolion.html"

class portfolio_detail(LoginRequiredMixin ,DetailView):
    model = models.Portfolio
    context_object_name = "Portfolio_detail"
    template_name = "user/portfolion_detail.html"
     
class portfolio_create(LoginRequiredMixin ,CreateView):
    model = models.Portfolio
    context_object_name = "Portfolio_detail"
    template_name = "user/portfolion_create.html"

class portfolio_file_add(LoginRequiredMixin ,CreateView):
    model = models.PortfolioFile
    context_object_name = "Portfolio_file_add"
    template_name = "user/portfolion_create.html"

class portfolio_delete(LoginRequiredMixin ,DeleteView):
    model = models.Portfolio
    context_object_name = "Portfolio_delete"
    template_name = "user/portfolion_delete.html"

class portfolio_file_delete(LoginRequiredMixin ,DeleteView):
    model = models.PortfolioFile
    context_object_name = "Portfolio_file_delete"
    template_name = "user/portfolion_delete.html"




     



    

# Create your views here.
