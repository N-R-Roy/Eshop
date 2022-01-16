from django import template

register = template.Library()


@register.filter("is_in_cart")
def is_in_cart(product, cart):
    if str(product.id) in cart:
        return True
    else:
        return False
