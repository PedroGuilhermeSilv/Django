

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=105)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_step = models.TextField()
    preparation_step_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # no momento da criação ele add uma data
    update_at = models.DateTimeField(auto_now=True) 
    is_publish = models.BooleanField(default=False)
    cover = models.ImageField(upload_to= 'recipes/cover/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True) # quando a categoria for apagada será setado NULL
# EDITED
# title description slug
# preparation_time preparation_time_unit
# servings servings_unit
# preparation_step
# preparation_step_is_html
# created_at updated_at
# is_published
# cover
# category (Relação)
# Author (Relação)
