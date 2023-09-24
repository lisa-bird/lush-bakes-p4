from django.shortcuts import render


def view_basket(request):
    ''' A view that shows the basket page'''

    return render(request, 'basket/basket.html')
