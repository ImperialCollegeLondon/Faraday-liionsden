from model_bakery.recipe import Recipe, foreign_key

from dfndb.models import Material, Parameter

parameter = Recipe(Parameter)

material = Recipe(Material)
