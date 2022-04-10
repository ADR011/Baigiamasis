from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 


class RegisterUserFor(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class: 'form-control'}))
    firs_name = forms.CharField(max_Lengh=50)
    last_name = forms.CharField(max_Lengh=50)


        class Meta:
        model = User
        fields = ('username', 'firs_name', 'last_name', 'email')