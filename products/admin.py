from django.contrib import admin
from .models import Product, Category, Wishlist, ProductReview, DiscountCode

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'get_products',
    )

    def get_products(self, obj):
        return ", ".join([str(product) for product in obj.products.all()])
    get_products.short_description = 'Products'

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'rating',
        'created_at',
    )
    ordering = ('created_at',)

class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'discount_percentage',
        'valid_from',
        'valid_to',
        'active',
    )
    list_filter = ('active',)

# Register the models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(DiscountCode, DiscountCodeAdmin)
