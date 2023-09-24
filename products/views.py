from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Lower
from .models import Product, Category


def products(request):
    ''' A view to show all products and sorting '''

    products = Product.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'sort' in request.GET:
            sort = request.GET['sort']

            if sort == 'price':
                if 'direction' in request.GET:
                    direction = request.GET['direction']
                    if direction == 'desc':
                        products = products.order_by('-price')
                    else:
                        products = products.order_by('price')

    current_sorting = f'{sort}_{direction}' 

    context = {
        'products': products,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context)


def product_description(request, product_id):
    ''' A view to show description of product/bake '''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_description.html', context)
