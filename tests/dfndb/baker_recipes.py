from model_bakery.recipe import Recipe, foreign_key, related

from dfndb.models import (
    Component,
    CompositionPart,
    Compound,
    Data,
    DataParameter,
    Method,
    Parameter,
    QuantityUnit,
)
from tests.management.baker_recipes import user

quantity_unit = Recipe(QuantityUnit)

compound = Recipe(Compound)

parameter = Recipe(Parameter, user_owner=foreign_key(user))

material = Recipe(Component, user_owner=foreign_key(user))

composition_part = Recipe(
    CompositionPart, material=foreign_key(material), compound=foreign_key(compound)
)

method = Recipe(Method, user_owner=foreign_key(user))

data = Recipe(Data, parameter=related(parameter), user_owner=foreign_key(user))

data_parameter = Recipe(
    DataParameter, data=foreign_key(data), parameter=foreign_key(parameter)
)
