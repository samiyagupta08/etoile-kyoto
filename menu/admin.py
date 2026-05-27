from django.contrib import admin
from .models import MenuItem

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'featured')
    list_filter = ('category', 'featured')
    search_fields = ('name', 'description')
