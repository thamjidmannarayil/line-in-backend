from django.urls import path
from .views import FAQListCreateAPIView, FAQDetailAPIView

app_name = 'faqs'
urlpatterns = [
    path('', FAQListCreateAPIView.as_view(), name='faq-list-create'),
    path('<int:pk>/', FAQDetailAPIView.as_view(), name='faq-detail'),
]
