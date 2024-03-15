from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe, Ingredient, RecipeIngredient
from django.contrib.auth.mixins import LoginRequiredMixin

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
# Create your views here.
