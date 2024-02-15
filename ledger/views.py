from django.shortcuts import render

def recipes_list(request):
    ctx = {
        "recipes": [
            "recipe 1",
            "recipe 2"
        ]
    }
    return render(request, "recipe_list.html", ctx)
# Create your views here.
