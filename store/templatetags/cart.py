from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product , cart):
    keys=cart.keys()
    for id in keys:
        if(int(id)==product.id):
            return True
    return False


@register.filter(name='cart_qnt')
def cart_qnt(product , cart):
    keys=cart.keys()
    for id in keys:
        if(int(id)==product.id):
            return cart.get(id)
    return 0

@register.filter(name='total_price')
def total_price(product , cart):
    return product.price * cart_qnt(product,cart)

@register.filter(name='total_cart_price')
def total_cart_price(product , cart):
    total=0;
    for p in product:
        total+=total_price(p,cart)
    return total



@register.filter(name='Rupees')
def Rupees(price):
    return "₹"+str(price)

# order total price
@register.filter(name='Multiply')
def Multiply(x,y):
    return x*y
