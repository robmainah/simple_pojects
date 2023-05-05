from django import template

register = template.Library()

@register.filter
def starts_with(text, starts):
    if text.startswith(starts):
        return True
    return False
