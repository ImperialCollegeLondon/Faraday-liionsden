from model_bakery.recipe import Recipe, foreign_key

from common.models import Org
from tests.management.baker_recipes import user

org = Recipe(Org, manager=foreign_key(user))