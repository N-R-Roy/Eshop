from django import template

register = template.Library()


@register.filter("is_in_cart")
def is_in_cart(product, cart):
    if str(product.id) in cart:
        return True
    else:
        return False


@register.filter("cart_in_quantity")
def cart_in_quantity(product_id, cart):
    return cart[str(product_id)]


@register.filter("total_price")
def total_price(product, cart):
    return product.price * cart[str(product.id)]


@register.filter("find_total")
def find_total(products, cart):
    total = 0
    for product in products:
        total = total + total_price(product, cart)

    return total


@register.filter
def convert_dict(value):
    return dict(value)



