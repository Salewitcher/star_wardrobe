from django.db import models
from django.contrib.auth.models import User  # For linking models to users
from django.db.models import Avg
from django.core.validators import MinValueValidator


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0)]
    )
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(0)]
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class Wishlist(models.Model):
    """
    A model to represent a user's wishlist
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wishlist")
    products = models.ManyToManyField(Product, blank=True, related_name="wishlisted_by")

    def __str__(self):
        return f"{self.user.username}'s Wishlist"


class ProductReview(models.Model):
    """
    A model for product reviews
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    review_text = models.TextField()
    rating = models.PositiveIntegerField()  # Ensures rating is between 1-5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"
    
    def save(self, *args, **kwargs):
        """
        Override save method to update product rating
        """
        super().save(*args, **kwargs)
        self.update_product_rating()

    def delete(self, *args, **kwargs):
        """
        Override delete method to update product rating when a review is removed
        """
        super().delete(*args, **kwargs)
        self.update_product_rating()

    def update_product_rating(self):
        """
        Updates the product's average rating based on existing reviews
        """
        avg_rating = self.product.reviews.aggregate(Avg("rating"))["rating__avg"]
        self.product.rating = round(avg_rating, 2) if avg_rating else None
        self.product.save()


class DiscountCode(models.Model):
    """
    A model to represent discount codes for products
    """
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, help_text="Enter discount as a percentage")
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Discount Code: {self.code} - {self.discount_percentage}%"
