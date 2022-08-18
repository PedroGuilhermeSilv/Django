from django.http import HttpResponse
from django.shortcuts import render

from recipes.factory import make_recipe
from recipes.models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request,'recipes/pages/home.html', context={'recipes': recipes})

def recipe(request, id):
    return render(request,'recipes/pages/recipe-views.html', context={'recipe': make_recipe(), 'if_detail_page': True,})

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={'recipes': recipes,
    })
