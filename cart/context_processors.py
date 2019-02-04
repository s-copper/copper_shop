from .cart import Cart


def cart(request):
    if not request.is_ajax():
        return {'cart': Cart(request)}
