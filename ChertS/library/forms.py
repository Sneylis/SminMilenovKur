from django import forms
from .models import *

class AddBookForm (forms.ModelForm):

    class Meta:
        model = Books
        fields = ['title', 'author', 'preview', 'photo', 'file', 'cat']
        widjets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'author': forms.TextInput(attrs={'class':'form-input'}),
            'preview': forms.Textarea(attrs={'cols':60,'rows':10}),
        }


