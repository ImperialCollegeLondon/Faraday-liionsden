from django.contrib.auth import get_user_model
from model_bakery.recipe import Recipe

User = get_user_model()
user = Recipe(User)
