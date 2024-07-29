from django.shortcuts import render, redirect, get_object_or_404
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

    return render(request,'recipe_app/add_recipe.html')



def search(request):
    query = request.GET.get('search')
    if query:
        
        if Recipe.objects.filter(recipe_name__icontains = query):
            recipes = Recipe.objects.filter(recipe_name__icontains = query)
        else:
            return render(request,'recipe_app/notfound.html')
        return render(request, 'recipe_app/search_results.html',{'recipes':recipes})
    

def view_recipe(request,recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_app/recipe_view.html',{'recipe':recipe})
    

