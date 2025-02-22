from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile, NewsletterSignup
from django.db.utils import IntegrityError
from django.utils import timezone


class UserProfileModelTest(TestCase):

    def setUp(self):
        """Create a user and its profile for testing"""
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.profile = self.user.profile  # UserProfile should be automatically created

    def test_user_profile_created_on_user_creation(self):
        """Test that a user profile is created automatically when a user is created"""
        self.assertIsNotNone(self.profile)
        self.assertEqual(self.profile.user, self.user)
        self.assertTrue(self.profile.first_purchase_discount)  # Default value should be True

    def test_user_profile_fields(self):
        """Test the fields of the user profile"""
        self.profile.default_phone_number = "1234567890"
        self.profile.default_street_address1 = "123 Test St"
        self.profile.default_town_or_city = "Test City"
        self.profile.save()

        # Fetch profile again and check if fields are correctly updated
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_phone_number, "1234567890")
        self.assertEqual(self.profile.default_street_address1, "123 Test St")
        self.assertEqual(self.profile.default_town_or_city, "Test City")

    def test_create_user_profile_signal(self):
        """Test that the post_save signal creates a profile for a new user"""
        user2 = User.objects.create_user(username="newuser", password="newpassword")
        # Profile should be automatically created when a new user is created
        self.assertTrue(hasattr(user2, 'profile'))  # Ensure the profile attribute exists
        self.assertEqual(user2.profile.first_purchase_discount, True)  # Check if default value is set

    def test_update_user_profile_signal(self):
        """Test that the profile is updated when the user is saved"""
        self.profile.default_phone_number = "9876543210"
        self.profile.save()

        # Ensure the profile is updated
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.default_phone_number, "9876543210")


class NewsletterSignupModelTest(TestCase):

    def setUp(self):
        """Create a newsletter signup instance"""
        self.signup = NewsletterSignup.objects.create(email="test@example.com")

    def test_newsletter_signup_creation(self):
        """Test that a newsletter signup is created successfully"""
        self.assertEqual(self.signup.email, "test@example.com")
        self.assertTrue(isinstance(self.signup.date_added, timezone.datetime))  # Check if date_added is set

    def test_unique_email_in_newsletter_signup(self):
        """Test that duplicate emails cannot be added to the newsletter signup"""
        with self.assertRaises(IntegrityError):
            NewsletterSignup.objects.create(email="test@example.com")  # Duplicate email should raise an IntegrityError

    def test_newsletter_signup_str(self):
        """Test the string representation of the NewsletterSignup"""
        self.assertEqual(str(self.signup), "test@example.com")
