from django import template

register = template.Library()


def trim(value):
    if len(value) > 6:
        return value[:6]
    return value

register.filter('trim', trim)


@register.filter
def trim_2(value):
    if len(value) > 10:
        return value[:10]
    return value

@register.simple_tag
def trim_2(value):
    if len(value) > 10:
        return value[:10]
    return value