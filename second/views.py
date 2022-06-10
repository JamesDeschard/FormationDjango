from re import template
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import ListView, DetailView

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from first.models import Movie
from .forms import MyExampleForm, MovieForm, CommentForm
from .models import Comment


class FilmView(View):
    template_name = 'films.html'

    def get(self, request, *args, **kwargs):
        context = {
            'films': Movie.objects.all(),
        }
        return render(request, self.template_name, context)



class FilmSearchView(View):

    template_name = 'films.html'

    def get(self, request, *args, **kwargs):
        search = request.GET.get('q')
        context = {
            'films': Movie.objects.filter(original_title__icontains=search),
        }
        return render(request, self.template_name, context)


class FilmDetailView(View):
    template_name = 'detail_film.html'

    def get_movie(self, id):
        return Movie.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id = kwargs['pk']
        movie=self.get_movie(id)
        comments = movie.comments.all()

        context = {
            'film': movie,
            'form': CommentForm(),
            'comments': comments,
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        id = kwargs['pk']
        movie = self.get_movie(id)
        form = CommentForm(request.POST)

        if form.is_valid():
            Comment.objects.create(text=form.cleaned_data['text'], movie=movie)
            comments = movie.comments.all()

            context = {
                'film': movie,
                'form': CommentForm(),
                'comments': comments,
            }

            return render(request, self.template_name, context)
    

class FilmCreateView(View):
    template_name = 'create_film.html'

    def get(self, request, *args, **kwargs):
        form = MovieForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films')
        else:
            return render(request, self.template_name, {'form': form})

class FilmDeleteView(View):
    template_name = 'delete_film.html'

    def get(self, request, *args, **kwargs):
        context = {
            'film': Movie.objects.get(id=kwargs['pk'])
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        Movie.objects.get(id=kwargs['pk']).delete()
        return redirect('films')

