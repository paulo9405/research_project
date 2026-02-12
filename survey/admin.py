from django.contrib import admin
from .models import SurveyResponse


@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    # Columns shown in the Admin list view
    list_display = ('full_name', 'reason', 'nationality', 'city', 'age', 'created_at')
    # Sidebar filter by reason
    list_filter  = ('reason',)
