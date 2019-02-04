from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Product
from cart.forms import CartAddForm, CartUpdateForm
from cart.cart import Cart


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    cart = Cart(request)
    price = cart.get_total_price()
    return render(request, 'shop/products/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddForm()

    return render(request, 'shop/products/detail.html',
                              {'product': product,
                               'cart_product_form': cart_product_form})

