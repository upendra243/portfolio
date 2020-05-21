import datetime

from django import template

register = template.Library()


def custom_lower(value):
    return value.lower()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


register.filter('abc', custom_lower)
