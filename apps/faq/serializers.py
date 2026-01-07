from rest_framework import serializers

from apps.faq.models import FrequentlyAskedQuestion


class FrequentlyAskedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestion
        fields = [
            'id',
            'question',
            'answer',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
