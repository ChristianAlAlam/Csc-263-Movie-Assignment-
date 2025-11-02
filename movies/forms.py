from django.forms import ModelForm
from .models import Movie
from django import forms

class MovieForm(ModelForm):
	class Meta:
		model = Movie
		fields = ['title', 'director', 'genre', 'release_year', 'description', 'rating']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'director': forms.TextInput(attrs={'class': 'form-control'}),
			'genre': forms.TextInput(attrs={'class': 'form-control'}),
			'release_year': forms.DateInput(attrs={'class': 'form-control', 'min': '1888', 'max': '2024', 'type': 'number' }),
			'description': forms.Textarea(attrs={'class': 'form-control'}),
			'rating': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0', 'max': '10'}),	
		}