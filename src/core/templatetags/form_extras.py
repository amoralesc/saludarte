from django import template
from django.forms.models import ModelChoiceIteratorValue

register = template.Library()


@register.filter
def get_fields(form, field_names):
    """
    Returns a list of the fields from a form given the field names.
    """

    fields = []
    field_names = field_names.split(",")

    for field in form:
        if field.name in field_names:
            fields.append(field)

    return fields


@register.filter
def to_int(value):
    """
    Converts value to an integer.
    """

    if isinstance(value, ModelChoiceIteratorValue):
        return int(value.value)

    return int(value)
