from django import template 


register = template.Library()

@register.filter
def exclude_city(cities, city):
    return cities.exclude(id=city)