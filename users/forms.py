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
    option1 = forms.CharField(
                            max_length=128,
                            label="Варіант 2",
                            required= True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть варіант 2'}))
    option1 = forms.CharField(
                            max_length=128,
                            label="Варіант 3",
                            required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть варіант 3'}))
    option1 = forms.CharField( 
                            max_length=128,
                            label="Варіант 4",
                            required=False,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть варіант 4'}))
    class Meta:
        model = models.Poll
        fields = ["text"]

    def __init__(self, *args, **kwargs):
        super(AddPoll, self).__init__(*args, **kwargs)

        self.fields['text'].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Назва"
        })


class SinginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields = ("first_name", "last_name", "email", "username")
        

