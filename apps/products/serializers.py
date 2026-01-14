from rest_framework import serializers

from apps.authentication.serializers import UserSerializer
from .models import File, Product, Comment, Advertisement, Favorite, Categories


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'slug', 'description', 'icon']



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'images']
        read_only_fields = ['images']

class ProductListSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, source='file_set')
    rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'slug', 'name', 'price', 'files','synopsis', 'stock_available', 'availability', 'rating', 'review_count', 'is_favorite']

    @staticmethod
    def get_rating(obj):
        reviews = obj.product_comment.all()
        if reviews.exists():
            total_rating = sum([review.rating for review in reviews])
            return total_rating / reviews.count()
        return 0

    @staticmethod
    def get_review_count(obj):
        return obj.product_comment.count()

    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Favorite.objects.filter(user=request.user, product=obj).exists()
        return False

class ProductsSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, source='file_set')
    rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['slug', 'created_at', 'updated_at']

    @staticmethod
    def get_rating(obj):
        reviews = obj.product_comment.all()
        if reviews.exists():
            total_rating = sum([review.rating for review in reviews])
            return total_rating / reviews.count()
        return 0

    @staticmethod
    def get_review_count(obj):
        return obj.product_comment.count()

    @staticmethod
    def get_reviews(obj):
        comments = obj.product_comment.all()
        return CommentsSerializer(comments, many=True).data if comments.exists() else None

    def get_is_favorite(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Favorite.objects.filter(user=request.user, product=obj).exists()
        return False


class CommentsSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['author', 'message', 'rating', 'created_at']


class AdvertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['title', 'file', 'link']


class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), source='product', write_only=True
    )

    class Meta:
        model = Favorite
        fields = ['id', 'product', 'product_id', 'created_at']

