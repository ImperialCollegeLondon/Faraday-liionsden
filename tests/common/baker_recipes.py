from model_bakery.recipe import Recipe, foreign_key

from common.models import Org, Paper, Person
from tests.management.baker_recipes import user

org = Recipe(Org, manager=foreign_key(user))

paper = Recipe(Paper, user_owner=foreign_key(user))

person = Recipe(Person)
