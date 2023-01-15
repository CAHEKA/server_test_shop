from django.contrib import admin
from .models import Products, Feedbacks


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'inventory', 'updated_at')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Products, ProductAdmin)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('product', 'comment', 'one', 'two', 'three', 'four', 'five')

admin.site.register(Feedbacks, RatingAdmin)
