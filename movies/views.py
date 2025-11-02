from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import MovieForm
from .models import Movie


def index(request):
	movies = Movie.objects.all()
	return render(request,'index.html')

def add_movie(request):
	if request.method == 'POST':
		form = MovieForm(request.POST)
		if form.is_valid():
			movieform = form.cleaned_data
			title = movieform['title']
			director = movieform['director']
			genre = movieform['genre']
			release_year = movieform['release_year']
			description = movieform['description']
			rating = movieform['rating']
			Movie.objects.create(title=title,director=director,genre=genre,release_year=release_year,description=description,rating=rating)
			return render(request, 'index.html')
	else:
		form = MovieForm()
	return render(request, 'add_movie.html', {'form': form})


def edit_movie(request, movie_id):
	movie = Movie.objects.get(id=movie_id)
	if request.method == 'POST':
		form = MovieForm(request.POST, instance=movie)
		if form.is_valid():
			form.save()
			return render(request, 'index.html')
	else:
		form = MovieForm(instance=movie)
	return render(request, 'edit_movie.html', {'form': form, 'movie': movie})

def delete_movie(request, movie_id):
	movie = Movie.objects.get(id=movie_id)
	if request.method == 'POST':
		movie.delete()
		return render(request, 'index.html')
	return render(request, 'delete_movie.html', {'movie': movie})

def view_movie(request):
	movies = Movie.objects.all()
	return render(request, 'view_movie.html', {'movies': movies})

		