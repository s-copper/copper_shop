from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartUpdateForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_POST
def cart_add(request, product_id):
    if request.is_ajax():
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=1, update_quantity=False)
        price = cart.get_total_price_view()
        return JsonResponse({'price': price})


def cart_change_quantity(request):
    cart = Cart(request)
    book_id = request.POST.get('id')
    quantity = int(request.POST.get('count'))
    product = get_object_or_404(Product, id=book_id)
    cart.add(product=product, quantity=quantity, update_quantity=True)
    total_price = cart.get_total_price_view()
    book_total_price = format(product.price * quantity, '.2f')
    return JsonResponse({
        'total_price': total_price,
        'book_total_price': book_total_price,
        'id': book_id,
    })


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartUpdateForm(
            initial={
                'quantity': item['quantity'],
                'update': True
            })
    return render(request, 'cart/detail.html', {'cart': cart})

