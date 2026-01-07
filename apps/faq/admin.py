from django.contrib import admin

from apps.faq.models import FrequentlyAskedQuestion

class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(FrequentlyAskedQuestion, FrequentlyAskedQuestionAdmin)

