from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('newsletter-signup/', views.newsletter_signup, name='newsletter_signup'),
    path('newsletter-thank-you/', views.thank_you, name='thank_you'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
