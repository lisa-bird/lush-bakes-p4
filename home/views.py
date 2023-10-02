from django.shortcuts import render


def index(request):
    ''' A view to return the index page '''

    return render(request, 'home/index.html')


def review(request):
    ''' A view to return the review page '''

    return render(request, 'home/review.html')


def about(request):
    ''' A view to return the about page '''

    return render(request, 'home/about.html')
