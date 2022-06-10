from django import forms
from first.models import Movie
from .models import Comment


class MyExampleForm(forms.Form): #<form>
    name = forms.CharField(label='Enter your name', max_length=100) #<input>
    text = forms.CharField(label='Enter some text', max_length=100, widget=forms.Textarea) #<widget: textarea>
    age = forms.IntegerField(label='Enter your age') #<input>


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['movie']


