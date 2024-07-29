from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('add_recipe/',views.add_recipe, name='add_recipe'),
    path('search/',views.search, name='search'),
    path('<int:recipe_id>/recipe_view',views.view_recipe, name='view_recipe'),
]
