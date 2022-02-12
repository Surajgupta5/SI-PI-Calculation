from django.contrib import admin
from django.contrib.admin import register
from calculation.models import InterestData


@register(InterestData)
class InterestDataAdmin(admin.ModelAdmin):
    list_display = ["id", "loan_date", "release_date", "principal", "total", "is_deleted"]
