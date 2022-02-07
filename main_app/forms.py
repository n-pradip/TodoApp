from django import forms
from django.forms import ModelForm
from main_app.models import Todo

class TodoForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add task here...'}))
    class Meta:
        model = Todo
        fields = '__all__'

