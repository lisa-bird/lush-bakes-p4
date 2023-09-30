from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models.functions import Lower
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Category
from .forms import ProductForm


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


@login_required
def add_product(request):
    '''Page management - add bake to page'''
    if not request.user.is_superuser:
        messages.error(request, 'For admin use only!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added new bake!')
            return redirect(reverse('product_description', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'For admin use only!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(instance=product)
    messages.info(request, f'You are editing {product.name}')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated!')
            return redirect(reverse('product_description', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to update bake. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, 'For admin use only!')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
