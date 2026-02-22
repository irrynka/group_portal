from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from users import models
from users.forms import PortfolioFileForm, PortfolioUrlForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from users.forms import SinginForm
from django.urls import reverse_lazy

class Poll_List(ListView):
    model = models.Poll
    context_object_name = "Polls"
    template_name = "users/poll.html"
    paginate_by = 3

class Poll_Detail(LoginRequiredMixin ,DetailView):
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

class Portfolio_List(ListView):
    model = models.Portfolio
    context_object_name = "Portfolios"
    template_name = "user/portfolion.html"
    paginate_by = 2

    def get_queryset(self):
        return models.Portfolio.objects.prefetch_related('files').all()
     
class Portfolio_Create(LoginRequiredMixin, CreateView):
    model = models.Portfolio
    fields = ['title', 'description']
    template_name = "user/portfolion_create.html"
    success_url = reverse_lazy('portfolio_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Portfolio_Delete(LoginRequiredMixin ,DeleteView):
    model = models.Portfolio
    template_name = "user/portfolion_delete.html"
    success_url = reverse_lazy('portfolio_list')

###############################

class Portfolio_File_Add(LoginRequiredMixin ,CreateView):
    model = models.PortfolioFile
    form_class = PortfolioFileForm
    template_name = "user/portfolion_create.html"

    def form_valid(self, form):
        form.instance.portfolio_id = self.kwargs['portfolio_id']
        form.instance.type = 'file'
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('portfolio_list')

class Portfolio_Url_Add(LoginRequiredMixin ,CreateView):
    model = models.PortfolioFile
    form_class = PortfolioUrlForm
    template_name = "user/portfolion_create.html"

    def form_valid(self, form):
        form.instance.portfolio_id = self.kwargs['portfolio_id']
        form.instance.type = 'url'
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('portfolio_list')
        

class Portfolio_Media_Delete(LoginRequiredMixin ,DeleteView):
    model = models.PortfolioFile
    template_name = "user/portfolion_delete.html"
    success_url = reverse_lazy('portfolio_list')


###################################################################################

     

def Index(request):
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
