from django.contrib import admin
from .models import Orders


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number',
                    'full_address', 'status', 'created_at')


admin.site.register(Orders, OrderAdmin)
