from django.contrib import admin
from .models import ReservationTest


class ReservationTestAdmin(admin.ModelAdmin):
    list_display = ['user', 'documentation', 'created', 'updated', 'pyment', ]
    list_filter = ['created', 'updated']
    search_fields = ['user__username', 'documentation__title']
    date_hierarchy = 'created'


admin.site.register(ReservationTest, ReservationTestAdmin)
