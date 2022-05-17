from django import template

register = template.Library()


@register.filter
def get_fields(form, field_names):
    fields = []
    field_names = field_names.split(",")

    for field in form:
        if field.name in field_names:
            fields.append(field)

    return fields
