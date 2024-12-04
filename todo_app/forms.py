from .models import Todo
from django import forms

class task_form(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task']
