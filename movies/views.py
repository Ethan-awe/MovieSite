from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Movie

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'账户为 {username} 创建成功！')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'movies/register.html', {'form': form})

@login_required
def home(request):
    asia_movies = Movie.objects.filter(region='Asia')
    europe_movies = Movie.objects.filter(region='Europe')
    china_movies = Movie.objects.filter(region='China')
    context = {
        'asia_movies': asia_movies,
        'europe_movies': europe_movies,
        'china_movies': china_movies,
    }
    return render(request, 'movies/home.html', context)

@login_required
def asia_movies(request):
    movies = Movie.objects.filter(region='Asia')
    return render(request, 'movies/movie_list.html', {'movies': movies, 'title': '亚洲电影'})

@login_required
def europe_movies(request):
    movies = Movie.objects.filter(region='Europe')
    return render(request, 'movies/movie_list.html', {'movies': movies, 'title': '欧美电影'})

@login_required
def china_movies(request):
    movies = Movie.objects.filter(region='China')
    return render(request, 'movies/movie_list.html', {'movies': movies, 'title': '中国电影'})

@login_required
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})
