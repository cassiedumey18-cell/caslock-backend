from django.contrib import admin
from .models import Commission, Artwork, Price

@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'style', 'size', 'priority', 'status', 'created_at']
    list_filter = ['status', 'priority', 'style']
    search_fields = ['name', 'email']
    ordering = ['-created_at']

class PriceInline(admin.TabularInline):
    model = Price
    extra = 3

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'size', 'status']
    list_filter = ['status', 'category', 'size']
    search_fields = ['title']
    inlines = [PriceInline]