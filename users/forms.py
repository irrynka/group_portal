from django import forms
from django.contrib.auth.forms import UserCreationForm
from users import models
from django.contrib.auth.models import User

class AddPoll(forms.ModelForm):

    option1 = forms.CharField(
                            max_length=128,
                            label="Варіант 1",
                            required= True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть варіант 1'}))
    option2 = forms.CharField(
                            max_length=128,
                            label="Варіант 2",
                            required= True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть варіант 2'}))
    option3 = forms.CharField(
                            max_length=128,
                            label="Варіант 3",
                            required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть варіант 3'}))
    option4 = forms.CharField( 
                            max_length=128,
                            label="Варіант 4",
                            required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть варіант 4'}))
    class Meta:
        model = models.Poll
        fields = ["topic", "description"]

    def __init__(self, *args, **kwargs):
        super(AddPoll, self).__init__(*args, **kwargs)

        self.fields['topic'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Назва"
        })


class VoteForm(forms.Form):
    option = forms.ModelChoiceField(
        queryset=None,
        widget=forms.RadioSelect,
        empty_label=None,
        label="Оберіть варіант"
    )

    def __init__(self, poll, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['option'].queryset = poll.options.all()
        
class SinginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields = ("first_name", "last_name", "email", "username")
        

class GaleryForm(forms.ModelForm):
    class Meta:
        model = models.Galery
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control', 
                'accept': 'image/*,video/*'
            })
        }

class PortfolioFileForm(forms.ModelForm):
    class Meta:
        model = models.PortfolioFile
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={
                'class': 'form-control', 
            })
        }

class PortfolioUrlForm(forms.ModelForm):
    class Meta:
        model = models.PortfolioFile
        fields = ['url']
        widgets = {
            'url': forms.URLInput(attrs={
                'class': 'form-control', 
            })
        }

class AddGradeForm(forms.ModelForm):


    model = models.Grade
    fields = ['student', 'subject', 'value']
    widgets = {
        'student': forms.Select(attrs={'class': 'form-control'}),
        'subject': forms.Select(attrs={'class': 'form-control'}),
        'value': forms.NumberInput(attrs={
            'class': 'form-control',
            'min': 1,
            'max': 100,
            'placeholder': 'Оцінка (1-100)'
        })
    }

class AddAnonts(forms.ModelForm):
    model = models.Anonts
    fields = ['title', 'content']
    widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={
                            'class': 'form-control',
                            'rows': 3
        })
    }

class AddEvent(forms.ModelForm):
    class Meta:
        model = models.Event
        fields = ['title', 'description', 'date_start', 'date_end']
        widgets = {
            'title': forms.TextInput(attrs={'class' : 'form-control'}),
            'description': forms.Textarea(attrs={
                            'class': 'form-control',
                            'rows': 3
            }),
            'date_start': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'date_end': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        
        }

class AddTopic(forms.ModelForm):
    class Meta:
        model = models.Topic
        fields = ['category', 'title', 'description']
        widgets = {
            'caterogy': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={ 'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                            'class': 'form-control',
                            'rows': 3
        }),                            

            
        }
            
class AddMessage(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
        