from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from apps.faq.models import FrequentlyAskedQuestion
from apps.faq.serializers import FrequentlyAskedQuestionSerializer


class FAQListCreateAPIView(generics.ListCreateAPIView):
    queryset = FrequentlyAskedQuestion.objects.all().order_by('-created_at')
    serializer_class = FrequentlyAskedQuestionSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class FAQDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FrequentlyAskedQuestion.objects.all()
    serializer_class = FrequentlyAskedQuestionSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
