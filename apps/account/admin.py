from django.contrib import admin
from .models import Address, Profile, PersonalOffer


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_type', 'city', 'country', 'is_default', 'is_active')
    list_filter = ('address_type', 'is_default', 'is_active', 'country')
    search_fields = ('user__email', 'full_name', 'street_address', 'city')
    raw_id_fields = ('user',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'country', 'wallet_balance')
    search_fields = ('user__email', 'nickname', 'country')
    filter_horizontal = ('interests',)
    raw_id_fields = ('user',)


@admin.register(PersonalOffer)
class PersonalOfferAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'code', 'discount_percentage', 'valid_until', 'is_active')
    list_filter = ('is_active', 'valid_until')
    search_fields = ('user__email', 'title', 'code')
    raw_id_fields = ('user',)
