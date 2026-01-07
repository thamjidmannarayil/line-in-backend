from django.db import models

from utils.abstract_models import TimeStampedModel, ActiveModel

# Create your models here.


class FrequentlyAskedQuestion(TimeStampedModel, ActiveModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f"{self.question} -> {self.answer}"