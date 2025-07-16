from django import forms 
from .models import Todo

class PostForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('todo_title', 'todo_description')
    
