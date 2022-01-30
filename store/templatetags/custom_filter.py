from django import template

register = template.Library()


@register.filter("add_currency_sign")
def add_currency_sign(price):
    return "৳" + str(price)


@register.filter("multiply_price")
def multiply_price(price, quantity):
    return price * quantity

