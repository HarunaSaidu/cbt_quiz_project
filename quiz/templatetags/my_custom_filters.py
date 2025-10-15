from django import template

register = template.Library()

@register.filter
def div(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return None  # Handle cases where input is not a number or division by zero
    
@register.filter
def mod(value, arg):
    try:
        return int(value) % int(arg)
    except (ValueError, ZeroDivisionError):
        return None  # Handle cases where input is not a number or division by zero