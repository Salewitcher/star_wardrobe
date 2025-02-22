from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product

class BagViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.product = Product.objects.create(
            name='Test Product',
            price=10.99,
        )
        self.view_bag_url = reverse('view_bag')
        self.add_to_bag_url = reverse('add_to_bag', args=[self.product.id])
        self.adjust_bag_url = reverse('adjust_bag', args=[self.product.id])
        self.remove_from_bag_url = reverse('remove_from_bag', args=[self.product.id])
    
    def test_view_bag(self):
        response = self.client.get(self.view_bag_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag(self):
        response = self.client.post(self.add_to_bag_url, {'quantity': 1, 'redirect_url': self.view_bag_url})
        self.assertRedirects(response, self.view_bag_url)
        session = self.client.session
        self.assertIn(str(self.product.id), session.get('bag', {}))

    def test_adjust_bag(self):
        session = self.client.session
        session['bag'] = {str(self.product.id): 2}
        session.save()

        response = self.client.post(self.adjust_bag_url, {'quantity': 3})
        self.assertRedirects(response, self.view_bag_url)
        session = self.client.session
        self.assertEqual(session['bag'][str(self.product.id)], 3)

    def test_remove_from_bag(self):
        session = self.client.session
        session['bag'] = {str(self.product.id): 2}
        session.save()

        response = self.client.post(self.remove_from_bag_url)
        self.assertEqual(response.status_code, 200)
        session = self.client.session
        self.assertNotIn(str(self.product.id), session.get('bag', {}))
