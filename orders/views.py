from django.shortcuts import render,redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if len(cart) < 1:
        return redirect('shop:ProductList')
    else:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderItem.objects.create(order=order, product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                cart.clear()
                return render(request, 'orders/order/created.html', {'order': order})
        if request.user.is_authenticated:
            form = OrderCreateForm(
                initial={'first_name': request.user.first_name,
                         'last_name': request.user.last_name,
                         'email': request.user.email,
                         }
            )
        else:
            form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'cart': cart,
                                                            'form': form})
