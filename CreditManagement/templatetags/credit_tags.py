from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def euro(value):
    """Format for euro values."""
    v = "{}€{}".format('-' if value < 0 else '', intcomma(abs(value)))
    return mark_safe(v)


@register.filter
def negate(value):
    """Negates given numeric value."""
    return -value