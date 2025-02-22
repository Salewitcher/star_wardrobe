from django.test import TestCase
from django.contrib.auth import get_user_model
from decimal import Decimal
from products.models import Product
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem
from django.conf import settings


class OrderModelTest(TestCase):

    def setUp(self):
        # Set up a test user and product
        user = get_user_model().objects.create_user(
            username="testuser", password="password123"
        )
        self.user_profile = UserProfile.objects.create(
            user=user,
            default_street_address1="123 Test Street",
            default_town_or_city="Test City",
            default_country="GB"
        )
        self.product = Product.objects.create(
            name="Test Product", price=Decimal('10.00'), sku="TEST123"
        )

    def test_order_number_generation(self):
        """Test that an order number is generated when an Order is created."""
        order = Order.objects.create(
            user_profile=self.user_profile,
            full_name="John Doe",
            email="john.doe@example.com",
            phone_number="1234567890",
            country="GB",
            postcode="AB12 3CD",
            town_or_city="Test City",
            street_address1="123 Test Street",
        )
        self.assertTrue(order.order_number)
        self.assertEqual(len(order.order_number), 32)  # UUID length

    def test_order_total_calculation(self):
        """Test the calculation of order total, delivery cost, and grand total."""
        order = Order.objects.create(
            user_profile=self.user_profile,
            full_name="John Doe",
            email="john.doe@example.com",
            phone_number="1234567890",
            country="GB",
            postcode="AB12 3CD",
            town_or_city="Test City",
            street_address1="123 Test Street",
        )
        order_lineitem = OrderLineItem.objects.create(
            order=order,
            product=self.product,
            quantity=2,
        )
        order.update_total()

        self.assertEqual(order.order_total, Decimal('20.00'))  # 2 * 10.00
        self.assertEqual(order.delivery_cost, Decimal('2.00'))  # 10% delivery
        self.assertEqual(order.grand_total, Decimal('18.00'))  # order_total + delivery_cost - discount


class OrderLineItemModelTest(TestCase):

    def setUp(self):
        # Set up a test user and product
        user = get_user_model().objects.create_user(
            username="testuser", password="password123"
        )
        self.user_profile = UserProfile.objects.create(
            user=user,
            default_street_address1="123 Test Street",
            default_town_or_city="Test City",
            default_country="GB"
        )
        self.product = Product.objects.create(
            name="Test Product", price=Decimal('10.00'), sku="TEST123"
        )
        self.order = Order.objects.create(
            user_profile=self.user_profile,
            full_name="John Doe",
            email="john.doe@example.com",
            phone_number="1234567890",
            country="GB",
            postcode="AB12 3CD",
            town_or_city="Test City",
            street_address1="123 Test Street",
        )

    def test_lineitem_total_calculation(self):
        """Test that lineitem_total is correctly calculated based on product price and quantity."""
        lineitem = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=3,
        )
        self.assertEqual(lineitem.lineitem_total, Decimal('30.00'))  # 3 * 10.00

    def test_lineitem_total_update_on_save(self):
        """Test that the lineitem_total updates correctly when the quantity is changed."""
        lineitem = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
        )
        lineitem.quantity = 5
        lineitem.save()
        self.assertEqual(lineitem.lineitem_total, Decimal('50.00'))  # 5 * 10.00


class OrderModelTestWithDiscount(TestCase):

    def setUp(self):
        # Set up a test user and product
        user = get_user_model().objects.create_user(
            username="testuser", password="password123"
        )
        self.user_profile = UserProfile.objects.create(
            user=user,
            default_street_address1="123 Test Street",
            default_town_or_city="Test City",
            default_country="GB"
        )
        self.product = Product.objects.create(
            name="Test Product", price=Decimal('10.00'), sku="TEST123"
        )

    def test_order_total_with_discount(self):
        """Test the calculation of order total with discount."""
        order = Order.objects.create(
            user_profile=self.user_profile,
            full_name="John Doe",
            email="john.doe@example.com",
            phone_number="1234567890",
            country="GB",
            postcode="AB12 3CD",
            town_or_city="Test City",
            street_address1="123 Test Street",
            discount=Decimal('5.00'),
        )
        order_lineitem = OrderLineItem.objects.create(
            order=order,
            product=self.product,
            quantity=2,
        )
        order.update_total()

        self.assertEqual(order.order_total, Decimal('20.00'))  # 2 * 10.00
        self.assertEqual(order.grand_total, Decimal('15.00'))  # order_total + delivery_cost - discount


class OrderLineItemSaveTest(TestCase):

    def setUp(self):
        """Set up a test product and order."""
        user = get_user_model().objects.create_user(
            username="testuser", password="password123"
        )
        self.user_profile = UserProfile.objects.create(
            user=user,
            default_street_address1="123 Test Street",
            default_town_or_city="Test City",
            default_country="GB"
        )
        self.product = Product.objects.create(
            name="Test Product", price=Decimal('10.00'), sku="TEST123"
        )
        self.order = Order.objects.create(
            user_profile=self.user_profile,
            full_name="John Doe",
            email="john.doe@example.com",
            phone_number="1234567890",
            country="GB",
            postcode="AB12 3CD",
            town_or_city="Test City",
            street_address1="123 Test Street",
        )

    def test_lineitem_total_updates_on_save(self):
        """Test lineitem_total updates on save when quantity changes."""
        lineitem = OrderLineItem.objects.create(
            order=self.order,
            product=self.product,
            quantity=1,
        )
        self.assertEqual(lineitem.lineitem_total, Decimal('10.00'))
        lineitem.quantity = 3
        lineitem.save()
        self.assertEqual(lineitem.lineitem_total, Decimal('30.00'))
