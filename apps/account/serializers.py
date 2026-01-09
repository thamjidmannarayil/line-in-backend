from rest_framework import serializers
from apps.authentication.models import User
from apps.authentication.serializers import UserSerializer
from apps.products.models import Categories
from apps.products.serializers import CategorySerializer, CommentsSerializer
from apps.carts.serializers import OrderListSerializer
from .models import Address, Profile, PersonalOffer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id', 'address_type', 'full_name', 'phone_number', 
            'street_address', 'city', 'state', 'country', 
            'zip_code', 'is_default'
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    interests = CategorySerializer(many=True, read_only=True)
    interest_ids = serializers.PrimaryKeyRelatedField(
        queryset=Categories.objects.all(), 
        many=True, 
        write_only=True, 
        source='interests'
    )

    class Meta:
        model = Profile
        fields = [
            'user', 'nickname', 'date_of_birth', 'country', 
            'bio', 'interests', 'interest_ids', 'wallet_balance'
        ]
        read_only_fields = ['wallet_balance']

    def update(self, instance, validated_data):
        interests = validated_data.pop('interests', None)
        if interests is not None:
            instance.interests.set(interests)
        return super().update(instance, validated_data)


class PersonalOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalOffer
        fields = ['id', 'title', 'description', 'code', 'discount_percentage', 'valid_until']


class AccountOverviewSerializer(serializers.Serializer):
    profile = ProfileSerializer()
    recent_orders = OrderListSerializer(many=True)
    default_address = AddressSerializer()
    wallet_balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    referral_code = serializers.CharField(default="LINEIN-REF-123") # Placeholder
