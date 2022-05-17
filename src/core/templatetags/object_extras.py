from django import template

register = template.Library()


@register.filter
def get_attrs(object, attrs_names):
    attrs = []
    attrs_names = attrs_names.split(",")

    for attr in attrs_names:
        try:
            attrs.append(
                (
                    object._meta.get_field(attr).verbose_name,
                    getattr(object, attr),
                )
            )
        except Exception:
            pass

    return attrs
