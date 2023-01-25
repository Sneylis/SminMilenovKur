from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *

class AddNewsForm (forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'Text', 'news_photo', 'is_published']
        widjets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'Text': forms.Textarea(attrs={'cols':60,'rows':10}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label="Имя", widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label="Фамилия", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))




    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        widjets = {
            'username':forms.TextInput(attrs={'class':'form-input'}),
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email':forms.TextInput(attrs={'class':'form-input'}),
            'password1':forms.PasswordInput(attrs={'class':'form-input'}),
            'password2':forms.PasswordInput(attrs={'class':'form-input'}),
        }

