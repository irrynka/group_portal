from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from users import models
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from users.forms import SinginForm
from django.urls import reverse_lazy

class poll_list(ListView):
    model = models.Poll
    context_object_name = "Polls"
    template_name = "users/poll.html"
    paginate_by = 3

class poll_detail(LoginRequiredMixin ,DetailView):
    model = models.Poll
    context_object_name = "Poll_deteil"
    template_name = "users/poll.html"

# class poll_create(LoginRequiredMixin, CreateView):
#     model = models.Poll
#     context_object_name = "Poll_create"
#     template_name = "users/poll.html"


# class poll_vote

# class poll_result

###########################################################################

class portfolio_list(ListView):
    model = models.Portfolio
    context_object_name = "Portfolio"
    template_name = "user/portfolion.html"
    paginate_by = 2
     
class portfolio_create(LoginRequiredMixin ,CreateView):
    model = models.Portfolio
    context_object_name = "Portfolio_detail"
    template_name = "user/portfolion_create.html"

class portfolio_delete(LoginRequiredMixin ,DeleteView):
    model = models.Portfolio
    context_object_name = "Portfolio_delete"
    template_name = "user/portfolion_delete.html"

###############################

class portfolio_file_add(LoginRequiredMixin ,CreateView):
    model = models.PortfolioFile
    context_object_name = "Portfolio_file_add"
    template_name = "user/portfolion_create.html"

    def form_valid(self, form):
        form.instance.portfolio_id = self.kwargs['portfolio_id']
        form.instance.type = 'file'
        return super().form_valid(super)
    
    def get_success_url(self):
        return reverse_lazy('portfolio_list', kwargs={'portfolio_id': self.object.portfolio_id})

class portfolio_url_add(LoginRequiredMixin ,CreateView):
    model = models.PortfolioFile
    context_object_name = "Portfolio_url_add"
    template_name = "user/portfolion_create.html"

    def form_valid(self, form):
        form.instance.portfolio_id = self.kwargs['portfolio_id']
        form.instance.type = 'url'
        return super().form_valid(super)
    
    def get_success_url(self):
        return reverse_lazy('portfolio_list', kwargs={'portfolio_id': self.object.portfolio_id})

class portfolio_media_delete(LoginRequiredMixin ,DeleteView):
    model = models.PortfolioFile
    context_object_name = "Portfolio_file_delete"
    template_name = "user/portfolion_delete.html"


###################################################################################

     

def index(request):
    return render(request, "users/index.html")

###################################################################################


class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True

class CustomLogoutView(LogoutView):
    next_page = "login"

class RegisterView(CreateView):
    template_name = "auth/singin.html"
    form_class = SinginForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("login")
    

# Create your views here.
