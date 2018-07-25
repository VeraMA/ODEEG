from django.contrib import admin
from . models import DigitalContainer, Period


class PeriodAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'legacy_id',
        'name',
        'period_phase',
        'period_url',
        'period_start_year',
        'period_end_year'
    ]


admin.site.register(DigitalContainer)
admin.site.register(Period, PeriodAdmin)
