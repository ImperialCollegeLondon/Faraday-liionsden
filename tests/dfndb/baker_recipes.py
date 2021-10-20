from model_bakery.recipe import Recipe, foreign_key

from dfndb.models import Material, Parameter
from tests.management.baker_recipes import user

parameter = Recipe(Parameter, user_owner=foreign_key(user))

material = Recipe(Material, user_owner=foreign_key(user))
