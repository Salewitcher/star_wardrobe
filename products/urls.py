from django.urls import path
from . import views

urlpatterns = [
    # Product URLs
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

    # Wishlist URLs
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    # Add this URL pattern for 'add_to_wishlist'
    path('wishlist/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),

    # Discount Code URLs
    path('discount/', views.discount_codes, name='discount_codes'),
]