from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.authentication.models import User
from apps.carts.models import OrderDetail
from apps.carts.serializers import OrderListSerializer
from apps.products.models import Comment
from apps.products.serializers import CommentsSerializer
from .models import Address, Profile, PersonalOffer
from .serializers import (
    AddressSerializer, ProfileSerializer, 
    PersonalOfferSerializer, AccountOverviewSerializer,
    CommentsSerializer
)


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    """
    Get or update user profile information.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile


class AddressViewSet(viewsets.ModelViewSet):
    """
    Manage user addresses.
    """
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user, is_active=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderHistoryView(generics.ListAPIView):
    """
    List user's order history.
    """
    serializer_class = OrderListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return OrderDetail.objects.filter(user=self.request.user).order_by('-created_at')


class MyReviewsView(generics.ListAPIView):
    """
    List user's product reviews.
    """
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(author=self.request.user).order_by('-created_at')


class PersonalOffersView(generics.ListAPIView):
    """
    List available personal offers/discounts.
    """
    serializer_class = PersonalOfferSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PersonalOffer.objects.filter(user=self.request.user, is_active=True)


class AccountOverviewView(APIView):
    """
    Dashboard overview with profile, recent orders, and default address.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        profile, _ = Profile.objects.get_or_create(user=user)
        recent_orders = OrderDetail.objects.filter(user=user).order_by('-created_at')[:3]
        default_address = Address.objects.filter(user=user, is_default=True).first()
        
        data = {
            'profile': ProfileSerializer(profile, context={'request': request}).data,
            'recent_orders': OrderListSerializer(recent_orders, many=True).data,
            'default_address': AddressSerializer(default_address).data if default_address else None,
            'wallet_balance': profile.wallet_balance,
            'referral_code': "LINEIN-" + str(user.id).zfill(6)
        }
        return Response(data)
