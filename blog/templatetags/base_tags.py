from django import template
from blog.models import Categoty
register = template.Library()


@register.simple_tag
def title():
    return "ابیروگرام"


@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    return {
        "categoris" : Categoty.objects.filter(status=True)
    }
