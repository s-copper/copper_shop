from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for val in self.cart.values():
            val['price'] = Decimal(val['price'])
            val['total_price'] = val['price'] * val['quantity']
            yield val

    def __len__(self):
        return sum(val['quantity'] for val in self.cart.values())

    def get_total_price(self):
        total = 0
        for val in self:
            total += val['total_price']
        return total
        # return sum(Decimal(val['price']) * val['quantity'] for val in self.cart.values())

    def get_total_price_view(self):
        totalissshee = float()
        for product_id, value in self.cart.items():
            price = Decimal(value['price'])
            totalissshee += float(price * value['quantity'])
        return format(totalissshee, '.2f')

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
