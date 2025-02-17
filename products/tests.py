from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Product

class ProductsAppTests(TestCase):

    def setUp(self):
        """Set up test data before running each test."""
        self.category = Category.objects.create(name="Test Category")
        self.product = Product.objects.create(
            category=self.category,
            name="Test Product",
            description="Test Description",
            price=10.99
        )
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_product_model(self):
        """Test product model fields."""
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "Test Description")
        self.assertEqual(float(self.product.price), 10.99)

    def test_category_model(self):
        """Test category model fields."""
        self.assertEqual(self.category.name, "Test Category")

    def test_product_list_view(self):
        """Check if product list page loads correctly."""
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_view(self):
        """Check if product detail page loads correctly."""
        response = self.client.get(reverse('product_detail', args=[self.product.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_user_registration(self):
        """Test user registration form."""
        response = self.client.post(reverse('account_signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        })
        self.assertEqual(response.status_code, 200)  # Adjust based on expected redirect

    def test_checkout_view_requires_login(self):
        """Ensure checkout page is protected."""
        response = self.client.get(reverse('checkout'))
        self.assertNotEqual(response.status_code, 200)  # Should redirect to login
