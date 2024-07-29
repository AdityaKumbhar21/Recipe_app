from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    return render(request,'recipe_app/home.html',{'recipes':recipes})

def add_recipe(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe = data.get('recipe')
        recipe_img = request.FILES.get('recipe_image')
    

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe = recipe,
            recipe_image = recipe_img
        )

        return redirect('home')

    return render(request,'recipe_app/add_recipe.html')\
    

