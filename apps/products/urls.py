from django.urls import path
from .views import HomeView, ProductListView, ProductDetailView, ProductReviewsView, ReviewReplyView, AdvertiseView, FavoriteListCreateView, FavoriteDeleteView

app_name = 'product'
urlpatterns = [
    path('featured/', HomeView.as_view(), name='home'),
    path('advertisement/', AdvertiseView.as_view(), name='advertise-list'),
    path('list/', ProductListView.as_view(), name='product-list'),
    path('<slug:slug>/detail/', ProductDetailView.as_view(), name='product-detail'),
    path('<slug:service_slug>/reviews/', ProductReviewsView.as_view(), name='product-reviews'),
    path('reviews/<int:comment_id>/reply/', ReviewReplyView.as_view(), name='review-reply'),
    path('favorites/list-create/', FavoriteListCreateView.as_view(), name='favorite-list-create'),
    path('favorites/delete/<int:service_id>/', FavoriteDeleteView.as_view(), name='favorite-delete'),
]
