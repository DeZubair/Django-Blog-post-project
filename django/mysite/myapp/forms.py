from django import forms
from django.forms.models import ModelForm 
from .models import Contact


class Contact_form(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name',
                'last_name',
                'email',
                'phone',
                'message',]

'''
class Contact(forms.Form):
    First_name = forms.CharField(label='First name', max_length='100')
    Lirst_name = forms.CharField(label='Lirst name', max_length='100')
    Email = forms.EmailField(label='Email', max_length='100')
    Phone = forms.IntegerField(label='Phone')
    Message = forms.CharField(label='Message', widget=forms.Textarea)
'''