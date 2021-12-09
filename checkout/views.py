
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K4bDAKvloDPj9mLnLK7RLpVRU2gccxuhyRcoV2tiSD6rTUrftNyCX8tn8zcNgZfxtzOp719nFToCrTrd8mZS6AY00Du2BU3AW',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)