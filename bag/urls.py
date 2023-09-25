from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>', views.add_item, name='add_item'),
    # path('amend_quantity/<item_id>', views.amend_quantity, name='amend_quantity'),
]
