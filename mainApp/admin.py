from django.contrib import admin
from .models import Tutorial


class TutorialAdmin(admin.ModelAdmin):
    # fields = ['tutorial_title',
    #           'tutorial_published',
    #           'tutorial_content']

    fieldsets = [
        ('Title/date', {'fields': ['tutorial_title', 'tutorial_published']}),
        ('Content', {'fields': ['tutorial_content']})
    ]


# Register your models here.
admin.site.register(Tutorial, TutorialAdmin)
