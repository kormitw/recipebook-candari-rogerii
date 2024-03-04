from django.shortcuts import render
from .models import Recipe, Ingredient, RecipeIngredient

def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {
        'recipes' : recipes
    }
    return render(request, "recipe_list.html", ctx)

def recipe(request, pk):
    ingredients = RecipeIngredient.objects.filter(recipe__name="<recipe.name>")
    ctx = {
         'ingredients' : ingredients   
    }
    return render(request, "recipe.html", ctx)

def recipe2(request, pk):
    ctx = {
         "name": "Recipe 2",
            "ingredients": [
                {
                    "name": "garlic",
                    "quantity": "1 head"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "vinegar",
                    "quantity": "1/2cup"
                },
                {
                    "name": "water",
                    "quantity": "1 cup"
                },
                {
                    "name": "salt",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "whole black peppers",
                    "quantity": "1 tablespoon"
                },
                {
                    "name": "pork",
                    "quantity": "1 kilo"
                }
            ],
            "link": "/recipe/2"
    }
    return render(request, "recipe2.html", ctx)
    '''
    "name": "Recipe 1",
            "ingredients": [
                {
                    "name": "tomato",
                    "quantity": "3pcs"
                },
                {
                    "name": "onion",
                    "quantity": "1pc"
                },
                {
                    "name": "pork",
                    "quantity": "1kg"
                },
                {
                    "name": "water",
                    "quantity": "1L"
                },
                {
                    "name": "sinigang mix",
                    "quantity": "1 packet"
                }
            ],
            "link": "/recipe/"
    '''
# Create your views here.
