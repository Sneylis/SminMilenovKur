from django import forms
from .models import *

class AddDocs (forms.ModelForm):

    class Meta:
        model = VacationFile
        fields = '__all__'
        widjets = {
            'FirstName': forms.TextInput(attrs={'class':'form-input'}),
            'SecondName': forms.TextInput(attrs={'class':'form-input'}),
            'About': forms.TextInput(attrs={'cols':60,'rows':10}),
        }


