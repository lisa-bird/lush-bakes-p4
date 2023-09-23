from django.shortcuts import render, get_object_or_404
from .models import Product


def products(request):
    ''' A view to show all products '''

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_description(request, product_id):
    ''' A view to show description of product/bake '''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_description.html', context)
