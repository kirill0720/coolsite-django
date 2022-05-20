from django import template
from women.models import *

register = template.Library()


@register.simple_tag(name='getposts')
def get_posts(cat_selected=0):
    if not cat_selected:
        return Women.objects.all()
    else:
        return Women.objects.filter(cat_id=Category.objects.get(slug=cat_selected).id)


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}
