from model_bakery.recipe import Recipe, foreign_key

from common.models import Org, Person, Reference
from tests.management.baker_recipes import user

org = Recipe(Org, manager=foreign_key(user))

reference = Recipe(Reference, user_owner=foreign_key(user))

person = Recipe(Person)
