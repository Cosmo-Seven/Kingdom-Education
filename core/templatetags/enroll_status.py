from django import template

register = template.Library()


@register.filter
def status_color(status):
    return {
        "pending":"warning",
        "approved":"success",
        "expired":"secondary",
        "cancelled":"danger"
    }.get(status.lower(), "light")