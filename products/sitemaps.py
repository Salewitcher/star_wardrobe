from django.contrib.sitemaps import Sitemap
from .models import Product

class ProductSitemap(Sitemap):
    
    changefreq = 'weekly'
    priority = 0.8  # Value between 0.0 and 1.0; 1.0 is the highest priority.

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
