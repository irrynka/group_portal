from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from users import models
from users.forms import PortfolioFileForm, PortfolioUrlForm, AddPoll, VoteForm, AddGradeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from users.forms import SinginForm
from django.urls import reverse_lazy
from django.contrib import messages

class Poll_List(ListView):
    model = models.Poll
    context_object_name = "polls"
    template_name = "users/poll.html"
    paginate_by = 3

class Poll_Detail(LoginRequiredMixin ,DetailView):
    model = models.Poll
    context_object_name = "poll"
    template_name = "users/poll_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = self.object

        if self.request.user.is_authenticated:
            context['has_voted'] = models.Vote.objects.filter(
                poll=poll,
                user=self.request.user
            ).exists()
        else:
            context['has_voted'] = False

        context['form'] = VoteForm(poll=poll)

        options_with_votes = []
        total_votes = poll.votes.count()

        for option in poll.options.all():
            vote_count = models.Vote.objects.filter(option=option).count()
            percentage = (vote_count / total_votes * 100) if total_votes > 0 else 0
            options_with_votes.append({
                "option": option,
                "count": vote_count,
                "percentage": round(percentage, 1)
            })
        
        context['options_with_votes'] = options_with_votes
        context['total_votes'] = total_votes

        return context

class Poll_Create(LoginRequiredMixin, CreateView):
    model = models.Poll
    form_class = AddPoll
    template_name = "users/poll_create.html"
    success_url = reverse_lazy('poll_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        poll = form.save()

        option1 = form.cleaned_data.get('option1')
        option2 = form.cleaned_data.get('option2')
        option3 = form.cleaned_data.get('option3')
        option4 = form.cleaned_data.get('option4')

        if option1:
            models.PollOption.objects.create(poll=poll, text=option1)
        if option2:
            models.PollOption.objects.create(poll=poll, text=option2)
        if option3:
            models.PollOption.objects.create(poll=poll, text=option3)
        if option4:
            models.PollOption.objects.create(poll=poll, text=option4)

        return super().form_valid(form)






class Poll_Vote(LoginRequiredMixin, View):
    def post(self, request, pk):
        poll = get_object_or_404(models.Poll, pk=pk)

        if models.Vote.objects.filter(poll=poll, user=request.user).exists():
            messages.error(request, 'Ви вже проголусували за цей варіант')
            return redirect('poll_detail', pk=pk)
        
        form = VoteForm(poll, request.POST)
        if form.is_valid():
            option = form.cleaned_data['option']
            models.Vote.objects.create(
                poll=poll,
                option=option,
                user=request.user
            )
            messages.success(request, "Голос зарахований")
        else:
            messages.error(request, "Оберіть варіант відповіді")
        
        return redirect('poll_detail', pk=pk)





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

class Grade_List(ListView):
    model = models.Grade
    context_object_name = 'grades'
    template_name = 'users/grade_list.html'
    paginate_by = 20

    def get_queryset(self):
        queryset = models.Grade.objects.select_related('student', 'subject').order_by('-created_at')
        student_id = self.request.GET.get('student')

        if student_id:
            queryset = queryset.filter(student_id=student_id)

        subject_id = self.request.GET.get('subject')
        
        if subject_id:
            queryset = queryset.filter(subject_id=subject_id)

        return queryset

class Grade_Create(LoginRequiredMixin, CreateView):
    model = models.Grade
    form_class = AddGradeForm
    template_name = 'user/grade_create.html'
    success_url = reverse_lazy('grade_list')

class Grade_Update(LoginRequiredMixin, UpdateView):
    model = models.Grade
    form_class = AddGradeForm
    template_name = 'user/grade_update.html'
    success_url = reverse_lazy('grade_list')

class Grade_Delete(LoginRequiredMixin, DeleteView):
    model = models.Grade
    template_name = 'user/grade_delete.html'
    success_url = reverse_lazy('grade_list')





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
