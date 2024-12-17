from django.contrib import admin

from .models import Choice, Question

admin.site.register(Choice)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "date_published")

    def date_published(self, obj):
        return obj.pub_date.strftime("%Y-%m-%d %I:%M %p")
    
    date_published.short_description = "Publication Date"
