from django import forms
from django.forms import ModelForm
from .models import Contacts

def ContactForm(ModelForm):
    fullname = forms.CharField()
    email = forms.EmailField()
    title= forms.TextInput()
    message= forms.Textarea()

    
    class Meta:
        model = Contacts
        fields = [
            'fullname',
            'email',
            'title',
            'message',
            
        ]


