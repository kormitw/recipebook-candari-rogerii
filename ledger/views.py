from django.shortcuts import render
from .models import Recipe, Ingredient, RecipeIngredient

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes' : recipes
    }
    return render(request, "recipe_list.html", ctx)

def recipe(request, pk):
    recipeName = Recipe.objects.get(pk = pk)
    ingredients = RecipeIngredient.objects.filter(recipe__name=recipeName)
    ctx = {
         'ingredients' : ingredients   
    }
    return render(request, "recipe.html", ctx)


# Create your views here.
