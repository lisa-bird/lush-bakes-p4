from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>', views.add_item, name='add_item'),
    path('amend/<item_id>', views.amend_quantity, name='amend_quantity'),
    path('delete/<item_id>', views.delete_item, name='delete_item'),
]