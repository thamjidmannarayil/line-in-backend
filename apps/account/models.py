from django.db import models
from apps.authentication.models import User
from apps.products.models import Categories
from utils.abstract_models import TimeStampedModel, ActiveModel


class Address(TimeStampedModel, ActiveModel):
    ADDRESS_TYPES = (
        ('home', 'Home'),
        ('office', 'Office'),
        ('other', 'Other'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses')
    address_type = models.CharField(max_length=20, choices=ADDRESS_TYPES, default='home')
    full_name = models.CharField(max_length=255, help_text="Receiver's full name")
    phone_number = models.CharField(max_length=20)
    street_address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.user.email} - {self.address_type} - {self.city}"

    def save(self, *args, **kwargs):
        if self.is_default:
            # Set all other addresses of this user to not default
            Address.objects.filter(user=self.user).update(is_default=False)
        super().save(*args, **kwargs)


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    interests = models.ManyToManyField(Categories, blank=True, related_name='interested_users')
    wallet_balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Profile of {self.user.email}"


class PersonalOffer(TimeStampedModel, ActiveModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='personal_offers')
    title = models.CharField(max_length=255)
    description = models.TextField()
    code = models.CharField(max_length=50, blank=True, null=True)
    discount_percentage = models.PositiveIntegerField(default=0)
    valid_until = models.DateTimeField()

    def __str__(self):
        return self.title
