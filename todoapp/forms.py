from django import forms
from django.db.models import fields
from .models import mytodo

class todoform(forms.ModelForm):
    task = forms.CharField(max_length = 100, widget=forms.TextInput(attrs = {
        'id': 'todoField', 'placeholder': 'Enter Task'}))
    class Meta:
        model = mytodo
        fields =['task']
 