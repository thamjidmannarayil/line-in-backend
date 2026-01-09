from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    ProfileDetailView, AddressViewSet, OrderHistoryView,
    MyReviewsView, PersonalOffersView, AccountOverviewView
)

router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='address')

app_name = 'account'

urlpatterns = [
    path('', AccountOverviewView.as_view(), name='overview'),
    path('profile/', ProfileDetailView.as_view(), name='profile-detail'),
    path('orders/', OrderHistoryView.as_view(), name='order-history'),
    path('reviews/', MyReviewsView.as_view(), name='my-reviews'),
    path('offers/', PersonalOffersView.as_view(), name='personal-offers'),
    path('', include(router.urls)),
]
