from django import template

register = template.Library()


@register.filter
def obj_key(obj, key):
    '''Returns the given key from a dictionary.'''
    return getattr(obj, key)
