from django import forms
from .models import *

class AddNewsForm (forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'Text', 'news_photo', 'is_published']
        widjets = {
            'title': forms.TextInput(attrs={'class':'form-input'}),
            'Text': forms.Textarea(attrs={'cols':60,'rows':10}),
        }


