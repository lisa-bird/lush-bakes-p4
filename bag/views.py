from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_bag(request):
    ''' A view that shows the basket page'''

    return render(request, 'bag/bag.html')


def add_item(request, item_id):
    ''' Add a product and quantity to the basket'''
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f'You have updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'You have added {product.name} to your basket')

    request.session['bag'] = bag
    return redirect(redirect_url)


# def amend_quantity(request, item_id):

#         product = get_object_or_404(Product, pk=item_id)
#         quantity = int(request.POST.get('quantity', 0))
#         bag = request.session.get('bag', {})

#         
# def delete_item():