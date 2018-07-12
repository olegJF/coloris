from django import forms
from .models import *


class NoteModelForm(forms.ModelForm):
    text = forms.CharField(label='Заметка', required=True,
                           widget=forms.TextInput(attrs={
                                                    "class": 'form-control'}))

    class Meta(object):
        model = Note
        fields = ('text', )
        exclude = ('unique_words',)