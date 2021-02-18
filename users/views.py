from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import favorite_movies
import requests


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for  {username}. You can now log in. ')
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html', {'favorite_movies': favorite_movies})


def searchbar(request):
    if request.method == 'GET':
        movie_name = request.GET.get('movie_title')

        searched_movie = requests.get(
            'http://www.omdbapi.com/?apikey=9a63b7fd&t='+movie_name).json()

        return render(request, 'users/home.html', {'searched_movie': searched_movie, 'movie_name': movie_name})


def add_to_fav(request):
    model = favorite_movies

    messages.success(
        request, f'added to favorite ')
    return render(request, 'users/home.html')
