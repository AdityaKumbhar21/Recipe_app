from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe = models.TextField(max_length=500)
    recipe_image = models.ImageField(upload_to='recipe_images/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.recipe_name}"
