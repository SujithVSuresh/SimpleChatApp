from django import forms
from django.forms import ModelForm, fields
from . models import *

class MessageForm(forms.ModelForm):

    class Meta:
        model = Messages
        widgets = {'room': forms.HiddenInput()}
        fields = '__all__'
        exclude = ['message_created_on']

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        widgets = {'created_by': forms.HiddenInput()}
        fields = '__all__'
        exclude = ['date_created']        