from django.core.exceptions import ValidationError
from molmass import Formula, FormulaError


def validate_formula(value):
    try:
        Formula(value).mass
    except FormulaError as e:
        raise ValidationError(f"{e} - Formula is not valid. Please check your formula.")
