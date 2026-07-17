from django.contrib import admin
from .models import Commission, Artwork

@admin.register(Commission)
class CommissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'style', 'size', 'priority', 'status', 'created_at']
    list_filter = ['status', 'priority', 'style']
    search_fields = ['name', 'email']
    ordering = ['-created_at']
    
@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'size', 'price', 'status']
    list_filter = ['status', 'category', 'size']
    search_fields = ['title']